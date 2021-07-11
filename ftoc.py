#攝氏轉換成華氏，華氏轉換為攝氏
check = input('請問您所在地區使用溫度為華氏還是攝氏？：')
if check == '攝氏':
	celsius = input('請輸入攝氏溫度：')
	celsius = float(celsius)
	Fahrenheit = celsius * 9 / 5 + 32
	print('華氏溫度為：',Fahrenheit)