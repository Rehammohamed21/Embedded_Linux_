#!/bin/bash


Create_ph_book()
{
	read -p "Please enter phone book name: " pb
	res=`ls | grep $pb | wc -w`				#search for the phone book
	if [ $res -gt 0 ]						#check if the phone book is exist 
	then
		echo "The phone book is already existing!"
	else
		touch $pb
		echo "Phone Book created successfully"
	fi	
}

Search_contact()
{
	read -p "Enter the name: " name 	
	res1=`cat $pb | grep $name | wc -w`			#search for the name
	if [ $res1 -gt 0 ]							#check if the name is exist 
	then
		cont=`cat $pb | grep $name`
		
		clear
		echo "Contact:" 
		echo "$cont"
	else
		echo "Name is not exist!"
	fi	
}

Add_contact()
{
	read -p "Enter the phone number: " ph_num 	
	res1=`cat $pb | grep $ph_num | wc -w`		#search for the number
	if [ $res1 -gt 0 ]							#check if the number is exist 
	then
		echo "phone number is already existing!"
	else
		read -p "Enter the name: " name
		clear
		echo "Contact Info:"
		echo "Name: $name";echo "Number: $ph_num"$'\n'
		echo "$name :  $ph_num" >> $pb			#append the contact info into the phone book
		echo "Contact Saved Successully"
	fi
}

Edit_contact()
{
	read -p "Enter the name: " name 	
	res1=`cat $pb | grep $name | wc -w`			#search for the name
	if [ $res1 -gt 0 ]							#check if the name is exist 
	then
		clear
		echo "Enter Modified Data"
		read -p "Name: " M_name
		read -p "Number: " M_num
		
		new=`echo "$M_name :  $M_num"`
		old=`cat $pb | grep $name`
		
		clear
		echo "Old Contact: $old"
		echo "New Contact: $new"$'\n'
		
		sed -i s/"$old"/"$new"/g $pb			#replace old data with modified data
		echo "Contact Modified Successfully" 
	else
		echo "Name is not exist!"
	fi
}

Remove_contact()
{
	read -p "Enter the name: " D_name 	
	res1=`cat $pb | grep $D_name | wc -w`		#search for the name
	if [ $res1 -gt 0 ]							#check if the name is exist 
	then
		cont_name=`cat $pb | grep $D_name`
		
		clear
		echo "Contact: $cont_name"$'\n'
		read -p "Enter the last 4 numbers: " D_num 
		res2=`cat $pb | grep $D_num | wc -w`
		echo "Do you want to delete this Contact?"
		read -p "Enter y for Yes or n for No: " reply
		if [ $reply == "y" ] && [ $res2 -gt 0 ]
		then
			cont_num=`cat $pb | grep $D_name | grep $D_num`
			sed -i -e s/"$cont_num"//g $pb			#delete contact
			sed -i /^$/d $pb
			echo $'\n'"Contact Deleted Successfully" 
		elif [ $res2 -le 0 ]
		then
			echo "Wrong number"	
		fi
	else
		echo "Name is not exist!"
	fi
	
}

View_ph_book()
{
	
	cat $pb						#display phone book
	
}


flag=0
while [ $flag -eq 0 ]
do
	clear 
	echo "Welcome to The Phone Book"
	echo "1. Create New Phone Book"
	echo "2. Search Phone Book"
	read -p "Please enter your choise number: " choice
	if [ $choice == 1 ]
	then
		clear
		Create_ph_book
	elif [ $choice == 2 ]
	then
		clear
		read -p "Enter phone book name: " pb
		res=`ls | grep $pb | wc -w`		#search for the phone book
		if [ $res -gt 0 ]				#check if the phone book is exist 
		then
			while [ 1 ]
			do
				clear
				echo "Welcome to The Phone Book"
				echo "1. Search Contacts"
				echo "2. Add a Contact"
				echo "3. Edit Contact"
				echo "4. Remove Contact"
				echo "5. View Phone Book"
				echo "6. Quit"$'\n'
				read -p "Please enter your choise number: " num_ch
				clear
				
				case $num_ch in 
					1) Search_contact ;;
					2) Add_contact ;;
					3) Edit_contact ;;
					4) Remove_contact ;;
					5) View_ph_book ;;
					6) break ;;
					*) echo "Wrong Choice!" ;;
				esac

				echo $'\n'"Press 6 to Quit, anything else to return to main menu " 
				read ch
				if [ $ch -eq 6 ]
				then
					break 
				fi
			done 
			flag=1
		else
			echo "File is not exist!"
			echo "Do you want to create one?"
			read -p "Enter y for Yes or n for No: " rep
			if [ $rep == "y" ]
			then
				clear
				Create_ph_book
			else
				break
			fi
		fi
	else
		echo "Wrong Choice!"
		sleep 1
	fi
done