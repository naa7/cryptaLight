import requests, json, time, sys, os
from cryptaLight_coins_list import coins_list

def curl_coin(url):
	response = requests.get(url)
	response_json = json.loads(response.text)
	symbol = response_json[0]['symbol']
	price = response_json[0]['current_price']
	price_change_percentage_24h = response_json[0]['price_change_percentage_24h']
	return (symbol, round(price,10),round(price_change_percentage_24h,3))


def clear():
	os.system('clear')


def coin_price():
	try:
		counter = 0
		current_price = 0
		previous_price = 0
		current_price_position = 0
		previous_price_position = 0
		price_list = []
		coins_list_size = len(coins_list)

		print("+==========================+")
		print("|         \033[33;1;82mCryptaLight\033[0m      |")
		print("+==========================+")
		print("|\033[36;1;82m⇅\033[0m | \033[36;1;82mCoin\033[0m    |       \033[36;1;82mPrice\033[0m |")
		print("+==========================+")

		while True:
			for coin in coins_list:
				url = str("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=")+str(coin)
				name = str(curl_coin(url)).replace("'", "")
				name = list(name[1:-2].split(','))
				price_list.append(name[1])

				if len(price_list) > coins_list_size and len(price_list) <= (coins_list_size*2):
					current_price_position = int(coins_list_size+counter)
					previous_price_position = int(current_price_position - coins_list_size)
					previous_price = float(price_list[previous_price_position])
					current_price = float(price_list[current_price_position])

				if len(name[0]) == 7:
					name[0] = str(name[0]+"")
				elif len(name[0]) == 6:
					name[0] = str(name[0]+" ")
				elif len(name[0]) == 5:
					name[0] = str(name[0]+"  ")
				elif len(name[0]) == 4:
					name[0] = str(name[0]+"   ")
				elif len(name[0]) < 4:
					name[0] = str(name[0]+"    ")

				if float(name[2]) > 0:
					if (current_price > previous_price):
						print(str('|\033[32;1;5m🡅\033[0m | \033[32;1;82m'+name[0].upper()+'\033[0m') + " | \033[32;1;82m" + str(name[1].rjust(11))+ "\033[0m |")
					elif (current_price < previous_price):
						print(str('|\033[31;1;5m🡇\033[0m | \033[32;1;82m'+name[0].upper()+'\033[0m') + " | \033[32;1;82m" + str(name[1].rjust(11))+ "\033[0m |")
					else:
						print(str('|\033[32;1;82m🡅\033[0m | \033[32;1;82m'+name[0].upper()+'\033[0m') + " | \033[32;1;82m" + str(name[1].rjust(11))+ "\033[0m |")
				else:
					if (current_price < previous_price):
						print(str('|\033[31;1;5m🡇\033[0m | \033[31;1;82m'+name[0].upper()+'\033[0m') + " | \033[31;1;82m" + str(name[1].rjust(11))+ "\033[0m |")
					elif (current_price > previous_price):
						print(str('|\033[32;1;5m🡅\033[0m | \033[31;1;82m'+name[0].upper()+'\033[0m') + " | \033[31;1;82m" + str(name[1].rjust(11))+ "\033[0m |")
					else:
						print(str('|\033[31;1;82m🡇\033[0m | \033[31;1;82m'+name[0].upper()+'\033[0m') + " | \033[31;1;82m" + str(name[1].rjust(11))+ "\033[0m |")


				counter = counter + 1

				if counter < coins_list_size:
					print("+--+---------+-------------+")

				if len(price_list) == (coins_list_size*2):
					del price_list[0:coins_list_size]

			print("+==========================+")
			print("")
			print("+==========================+")
			print("|       \033[33;1;82mQuit: ctrl+c\033[0m       |")
			print("+==========================+")

			sys.stdout.write("\033[4A\033[K\r")

			for i in range(121):
				if i < 120:
					print("|      \033[36;1;82mUpdating in",str(120-i).rjust(2)+'s', "\033[0m    |",end='\r')
				else:
					print("|         \033[36;1;5mUpdating...\033[0m      |",end='\r')

				time.sleep(1)

			counter = 0
			lines_value = coins_list_size*2
			command = "\033["+str(lines_value)+"A\r"
			sys.stdout.write(command)

	except (KeyboardInterrupt, ConnectionError, Exception) as e:
				clear()
				sys.exit(0)
def main():
	coin_price()

if __name__ == "__main__":
	main()
