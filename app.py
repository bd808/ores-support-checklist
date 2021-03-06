# -*- coding: utf-8 -*-
#
#
# Copyright (C) 2017 Bryan Davis and contributors
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
"""ORES support checklist app"""

import flask
import os
import json
import werkzeug.contrib.fixers
import time


app = flask.Flask(__name__)
app.wsgi_app = werkzeug.contrib.fixers.ProxyFix(app.wsgi_app)


@app.route('/')
def index():
    """Application landing page."""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')
    data = json.load(open(json_url))
    wikis = data['data']
    update = time.strftime("%d %B %Y %H:%M:%S UTC",
                           time.gmtime(data['timestamp']))
    return flask.render_template('index.html', wikis=wikis, update=update)
