cd %USERPROFILE%\an-farmview

git pull
poetry install
poetry run python -u -m an_farmview.client.envmonitor
poetry run python -u -m an_farmview.client.ubl