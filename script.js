const txt = '{
	"id": 1
	"first_name" "John",
	"last_name": "Doe",
	"email": "johndoe@mail.com"
}'

let obj = JSON.parse(txt);
document.write(obj.first_name);