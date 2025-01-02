#! /bin/bash
curl -X POST -H 'Content-Type: application/json' -d '{"user_email": "test@test.com"}' http://localhost:8000/users/register
response=$(curl -X POST -H 'Content-Type: application/json' -d '{"user_email": "test@test.com", "title":"Test","survey_structure":{"questions":[{"required":true,"question":"test_text","question_type":"text","details":""},{"required":true,"question":"test_number","question_type":"number","min_value":0,"max_value":10},{"required":true,"question":"test_single","question_type":"single","choices":["a","b","c"]},{"required":true,"question":"test_multi","question_type":"multi","choices":["a","b","c"]},{"required":true,"question":"test_binary","question_type":"binary","choices":["Yes","No"]},{"required":true,"question":"test_scale","question_type":"scale"},{"required":true,"question":"test_slider","question_type":"slider","min_value":0,"max_value":10,"precision":1}, {"required":true,"question":"test_list","question_type":"list","choices":["list_1","list_2","list_3"]},{"required":false,"question":"test_rank","question_type":"rank","choices":["rank_1","rank_2","rank_3"]}]},"uses_cryptographic_module":false,"ring_members":[]}' http://localhost:8000/surveys/create)
survey_code=$(echo $response | jq -r '.survey_code')
export SURVEY_CODE_1=$survey_code
echo "Survey code saved to environment variable: $SURVEY_CODE_1"

response=$(curl -X POST -H 'Content-Type: application/json' -d '{"user_email": "test@test.com", "title":"Test","survey_structure":{"questions":[{"required":true,"question":"test_text","question_type":"text","details":""},{"required":false,"question":"test_number","question_type":"number","min_value":0,"max_value":10},{"required":false,"question":"test_single","question_type":"single","choices":["a","b","c"]},{"required":false,"question":"test_multi","question_type":"multi","choices":["a","b","c"]},{"required":false,"question":"test_binary","question_type":"binary","choices":["Yes","No"]},{"required":false,"question":"test_scale","question_type":"scale"},{"required":false,"question":"test_slider","question_type":"slider","min_value":0,"max_value":10,"precision":1}]},"uses_cryptographic_module":false,"ring_members":[]}' http://localhost:8000/surveys/create)
survey_code=$(echo $response | jq -r '.survey_code')
export SURVEY_CODE_2=$survey_code
echo "Survey code saved to environment variable: $SURVEY_CODE_2"

curl -X POST -H 'Content-Type: application/json' -d '{"user_email": "test@test.com", "survey_code": "'$SURVEY_CODE_2'", "is_enabled": false}' http://localhost:8000/surveys/set-enabled
