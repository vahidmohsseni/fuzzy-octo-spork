import requests
from bs4 import BeautifulSoup as soup
import re

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, Response
)

bp = Blueprint('api', __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/link", methods=["POST"])
def get_the_link():
    if request.method == "POST":
        l = request.form.get("link")
        # print(request.form.get("link"))
        link = look_for_mp3(l)

        return render_template("result.html", link = link)

    return "NOT FOUND"


def look_for_mp3(link):

    try:

        res = requests.get(link)

        # print(res.text)
        s = soup(res.text, 'html.parser')
        pattern = re.compile('http.*\.mp3', re.MULTILINE)

        for a in s.findAll("script", text=pattern):
            match = pattern.search(a.text)
            if match:
                # print(match)
                mp3_link = match.group(0)
                # print(mp3_link)

                return mp3_link
        return None
    except:
        return None
