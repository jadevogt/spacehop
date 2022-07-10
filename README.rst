#####################
Space Hop Backend API
#####################
.. |audio test| image:: https://github.com/jadevogt/spacehop-api/actions/workflows/test_audio.yml/badge.svg
   :height: 20
.. |characters test| image:: https://github.com/jadevogt/spacehop-api/actions/workflows/test_characters.yml/badge.svg
   :height: 20
.. |events test| image:: https://github.com/jadevogt/spacehop-api/actions/workflows/test_events.yml/badge.svg
   :height: 20
.. |images test| image:: https://github.com/jadevogt/spacehop-api/actions/workflows/test_images.yml/badge.svg
   :height: 20
.. |scenes test| image:: https://github.com/jadevogt/spacehop-api/actions/workflows/test_scenes.yml/badge.svg
   :height: 20
|audio test|
|characters test|
|events test|
|images test|
|scenes test|

********
Overview
********
WIP Backend for an upcoming web adaptation of the visual novel project 
`Space Hop <https://curryswirl.itch.io/space-hop-episode-1>`_. Once complete,
this API will allow a front-end management tool to perform CRUD operations and
support future changes or expansions to the scope of the visual novel. The
actual presentation of the visual novel will be handled by an HTML5 & JS web
application.

Ultimately, this should be easily adaptable for use with similar web-based
storytelling projects.

*********
Structure
*********
The narrative is split up into Chapters and Scenes. Chapters are linked to an
arbitrary number of Scenes, which themselves are linked to a sequence of Events.
The following are considered to be Events:

* Displaying a textbox
* Printing longer-form text across the screen
* Updating the background image
* Swapping or removing characters from the scene
* Starting a background audio track
* Stopping a background audio track
* Playing a sound effect
* Pausing for a specified period of time

The actual implementation and timing of these events is outside of the scope of
the API, so they are purposefully left vague. Events are sequenced out discretely
with the intention of making the story easily adapted to a text-only script for
the purposes of accessibility, search capabilities, or conversion into other formats.


*******
Roadmap
*******
* Database schema
* Read-only access via REST API
* Read-write access via REST API with authentication
* Support for uploading and managing image files
* Support for uploading and managing audio files
* Additional features if requested


******************
Build instructions
******************
If you would like to test the API locally, perform the following:

* Make sure you have Python 3.10 or later
* Run ``git clone https://github.com/jadevogt/spacehop.git``
* ``cd`` into ``spacehop``
* If you have Poetry installed, run ``poetry install`` to install dependencies

  * Otherwise, run ``python3 -m pip install .`` to install them

* Run ``python3 manage.py makemigrations``
* Run ``python3 manage.py migrate``
* Start the local test server with ``python3 manage.py runserver``

Deployment is outside of the scope of this file, please see
`the official Django documentation
<https://docs.djangoproject.com/en/4.0/howto/deployment/>`_ for deployment instructions.
