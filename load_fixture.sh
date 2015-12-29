#!/usr/bin/env bash

PORT=${1}

../appcfg.py upload_data --config_file=./loaderer/lesson.py --filename=./fixtures/lekcje.csv --kind=Lesson --url=http://localhost:"${PORT}"/_ah/remote_api chzis

../appcfg.py upload_data --config_file=./loaderer/.py --filename=./fixtures/piekary_kamien_glosiciele.csv.csv --kind=CongregationMember --url=http://localhost:"${PORT}"/_ah/remote_api chzis
