#!/bin/bash

echo "Автор: Львова Александра группа 727-1"

echo "Программа поиска файла и вывода информации о нём"

answer="y"



while [ "$answer" != "n" ]

do
	
echo "Введите имя файла"
	
	read filename

	if [ ! -f "$filename" ];
	
	then
		
		echo "Файл не существует"
		
		continue
	
fi

	
	stat --format="Имя файла: %n" "$filename"
	
	stat --format="Тип файла: %F" "$filename"
	
	stat --format="Размер файла: %s байт" "$filename"
	
	stat --format="Владелец файла: %U" "$filename"
	
	stat --format="Права доступа: %A" "$filename"
	
	stat --format="Дата создания: %w" "$filename"

	
	
	echo "Продолжать? y/n"
	
	read answer
	

	while [ "$answer" != "y" ] && [ "$answer" != "n" ]
	
	do
		
		echo "Продолжать? y/n"
		
		read answer
	
	done

done
