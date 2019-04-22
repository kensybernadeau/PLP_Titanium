
import titanium_parser

TParser = titanium_parser.getparser()
while True:
    try:
        parse_in = input('IN ->')
        TParser.parse(parse_in)
    except (EOFError, KeyboardInterrupt):
        break


