
	
	


def test_login_no_email(supply_url):
	url = supply_url + "/login/" 
	data = {}
	resp = requests.post(url, data=data)
	assert resp.status_code == 404, resp.text
	
	