import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)

response = br.open("http://getit.sv.comcast.com/m/8380519981420811112")

print response.read()