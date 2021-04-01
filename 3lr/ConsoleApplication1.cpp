//15. Напишите программу, в которой создается символьный массив для записи текста.
//Подсчитать для записанного в массиве текста количество слов и длину каждого слова.Словами
//считать набор символов между пробелами

#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
    char* buffer = new char[50];
    for (size_t i = 0; i < 50; i++)
        buffer[i] = 0;
    cout << "Input text: ";
    cin.getline(buffer, 50);

    int words_counter = 0;
    int word_length_counter = 0;
    const char* format_str_for_digit = "%d ";

    _asm {
        mov ecx, 50
        mov esi, buffer
        buffer_loop:
            mov eax, 50
            sub eax, ecx
            mov al, [esi + eax]
            cmp al, 32 // todo
            jne not_space
        its_space:
            inc words_counter
            push ecx
            push esi
            push eax
            push word_length_counter
            push format_str_for_digit
            call printf
            add esp, 8
            pop eax
            pop esi
            pop ecx
            mov word_length_counter, 0
            jmp next_char
        not_space:
            cmp al, 0 // todo
            jne not_zero
        its_zero:
        inc words_counter
            push ecx
            push esi
            push eax
            push word_length_counter
            push format_str_for_digit
            call printf
            add esp, 8
            pop eax
            pop esi
            pop ecx
            jmp end_loop
        not_zero:
        smth_else:
            inc word_length_counter
        next_char:
        loop buffer_loop
        end_loop:
    };
    /*
    for (size_t i = 0; i < 50; i++) {
        char ch = buffer[i];
        if (ch == ' ') {
            words_counter += 1;
            cout << word_length_counter << ' ';
            word_length_counter = 0;
        }
        else if (ch == '\0') {
            words_counter += 1;
            cout << word_length_counter << ' ';
            break;
        }
        else
            word_length_counter += 1;
    }
    */
    cout << endl << "Words count: " << words_counter << endl;

}
