# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
from flask import Flask, request, redirect, url_for, render_template
from transcribe_audio_deepgram import extract_text_from_audio  # Import function for audio transcription
from speaker_analysis_gpt import analyse_conversation  # Import function for speaker analysis
import json
import os
import magic

app = Flask(__name__)


# Function to check if the file is an audio file based on MIME type
def is_audio(file_path):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_file(file_path)
    return file_mime_type.startswith('audio/')


@app.route("/")
def index():
    """Render the index.html template for the home page."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    """Handle the upload of a file."""
    form = request.form

    # Is the upload using Ajax, or a direct POST by the form?
    is_ajax = False
    if form.get("__ajax", None) == "true":
        is_ajax = True

    # Target folder for these uploads.
    target = "app/static/uploads"

    try:
        # Retrieve the uploaded file from the request.
        uploaded_file = request.files['file']

        # Check if a file was uploaded.
        if uploaded_file.filename != '':
            filename = uploaded_file.filename
            file_path = "/".join([target, filename])
            uploaded_file.save(file_path)

            # If the uploaded file is an audio file, perform transcription.
            if is_audio(file_path):
                # Transcription of the audio file
                transcription = extract_text_from_audio(file_path)
                os.remove(file_path)
                if transcription:
                    print("TRUEE")
                    # Get the base name of the original file (without extension)
                    file_name_without_extension = os.path.splitext(filename)[0]

                    # Create the new file name by appending the new extension
                    new_file_name = f"{file_name_without_extension}.txt"
                    file_path = "/".join([target, new_file_name])
                    with open(file_path, 'w') as f:
                        print("TRUEE")
                        f.write(transcription)
                        uploaded_file.save(file_path)

            # Perform speaker analysis and psychological insights on the uploaded file
            analysis_results = analyse_conversation(file_path)
            os.remove(file_path)  # Remove the uploaded file after analysis
            # return render_template('result.html', text=to_render)

        # If the upload was through Ajax, return the analysis results as JSON.
        if is_ajax:
            return ajax_response(True, analysis_results)
        # If not Ajax, redirect to the upload_complete route to display results.
        else:
            return redirect(url_for("upload_complete", results=analysis_results))

    except Exception as e:
        return ajax_response(False, str(e))


@app.route("/result/<results>")
def upload_complete(results):
    """Render the result.html template to display the analysis results."""

    # Replace newline characters with HTML line breaks
    to_render = results.replace("\n", "<br />")
    return render_template('result.html', text=to_render)


def ajax_response(status, msg):
    """Format the response as JSON for Ajax requests."""
    status_code = "ok" if status else "error"
    return json.dumps(dict(
        status=status_code,
        msg=msg,
    ))


parser = argparse.ArgumentParser(description="Uploadr")
parser.add_argument(
    "--port", "-p",
    type=int,
    help="Port to listen on",
    default=2005,
)
args = parser.parse_args()

if __name__ == '__main__':
    flask_options = dict(
        host='0.0.0.0',
        debug=True,
        port=args.port,
        threaded=True,
    )

    app.run(**flask_options)
