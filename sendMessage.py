import requests
import sys
import getopt

#This is the default base for Slack
def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('your end point',
                            data = payload)
    print(response.text)

def main(argv):
    message = ' '

    try: opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print('SlackMessage.py -m <message>')
        sys.exit(2)
    if len(opts) == 0:
        message = "<@U02C5AK2FC1> This is a test"
    for opt, argv in opts:
        if opt == '-h':
            print('SlackMessage.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
    send_slack_message(message)

if __name__ == '__main__':
    main(sys.argv)
