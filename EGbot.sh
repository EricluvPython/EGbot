#!/bin/bash

trap end_bot SIGINT	# customized ctrl+c message, but not required
function end_bot(){
	echo "Process successfully ended."
	exit
}


# beginning of the main code
echo "EGbot - AI powered email listening and autoreply program, by Eric Gao"
echo "Process starting..."

while [ true ]	# processes don't end unless killed
do
	declare -a imap_output	# declare an array variable (maybe not needed)
	mapfile -t imap_output < <(python3 imap_receiver_module.py | tr -d '()' | sed 's/[][]//g;s/, /\n/g')	# convert python list/tuple to bash array

	sender=$(echo ${imap_output[0]} | tr -d "'")	# variable for received email sender
	body=$(echo ${imap_output[1]} | tr -d "'")	# variable for received email content
	
	if [[ $sender != '' ]]	# when there is a new email
	then
		echo "Received email from: $sender"
		echo "Email content: $body"
		bot_response=$(python3 bot_module.py "$body")	# use the bot module to get response
		echo "Bot responded: $bot_response"

		sent_status=$(python3 smtp_sender_module.py "$sender" "$bot_response")	# send the message
		echo $sent_status
	fi
	echo "Sleeping for 5s..."
	sleep 5		# this is set to prevent server recognizing the machine as DOSing
done
