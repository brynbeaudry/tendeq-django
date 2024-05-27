
curl -X GET http://localhost:8000/api/users/ -H 'Accept: application/json' | jq .

curl -X GET http://localhost:8000/api/documents/ -H 'Accept: application/json' | jq .

curl -X GET http://localhost:8000/api/loans/ -H 'Accept: application/json' | jq .

 curl -X POST -d "grant_type=password&username=lender1&password=defaultpassword" -u"tendeq:ZtGKB7Oio3HlkO8GPkeyB5YTJpmnNIhkOG8oQHMUdA5cDQRumv6AewoMP8nNLNx2Lyk5fSx31u2Fu1M8LaWl1Pq9MSc1v4oCtacTi9HH7GlxI2zc9pYevIszpK3ZekDO" http://localhost:8000/o/token/

curl -X POST http://localhost:8000/o/token/ \
     -H "Content-Type: application/json" \
     -d '{
         "grant_type": "password",
         "username": "lender1",
         "password": "defaultpassword",
         "client_id": "tendeq",
         "client_secret": "ZtGKB7Oio3HlkO8GPkeyB5YTJpmnNIhkOG8oQHMUdA5cDQRumv6AewoMP8nNLNx2Lyk5fSx31u2Fu1M8LaWl1Pq9MSc1v4oCtacTi9HH7GlxI2zc9pYevIszpK3ZekDO"
     }'

curl -X POST http://localhost:8000/o/token/ \
     -H "Content-Type: application/json" \
     -d '{
         "grant_type": "password",
         "username": "lender1",
         "password": "defaultpassword"
     }'