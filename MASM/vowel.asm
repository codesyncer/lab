.model small
.stack
.data
    vowels db "AEIOUaeiou"
    str db "iSRINaG$"
.code 
    mov ax, @data
    mov ds, ax
    mov si, -1
    mov dl, '0'
    loopi:
        inc si
        mov al, str[si]
        cmp al, '$'
        je outi
        mov cx, 10
        loopj:
            mov bx, cx
            cmp al, vowels[bx-1]
            je incr
            loop loopj
        dec dl
    incr:
        inc dl
    jmp loopi
outi:
    mov ah, 2h
    int 21h
    mov ah, 4ch
    int 21h
end