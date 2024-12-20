import argparse


argparser = argparse.ArgumentParser(description="Auto update DNS A-record with cloudflare api")
argparser.add_argument("-t", "--token", required=True, type=str, help="Token to access the cloudflare api")
argparser.add_argument("-z", "--zone", required=True, type=str, help="Cloudflare zone id")
argparser.add_argument("-r", "--record", required=True, type=str, nargs="+", help="DNS records names")
argparser.add_argument("-d", "--delay", required=False, type=int, help="Delay between record updates in seconds (default 30)")
argparser.add_argument("-A", "--autoexit", action="store_true", help="Exit programm if an error occurred updating the record")
argparser.add_argument("-v", "--verbose", action="store_true", help="More verbose output")


args = argparser.parse_args()