format PE

section '.data' writeable

arr db 10101010b, 01010101b, 11110000b, 00001111b

section '.text' executable
entry start
start:
        mov esi, arr
        mov ecx, 4
        mov eax, 0
        mov ebx, 0
        mov edx, 0
        cycle:
                lodsb
                mov dl, al
                and al, 00000010b
                cmp al, 0
                je empty
                shr dl, 1
        empty:
                add ebx, edx
        continue:
                loop cycle

ret

