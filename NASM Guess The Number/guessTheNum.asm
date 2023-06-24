;;; System call variables
SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1
STDERR equ 2

;;; Constants section
section .data
    ;;; Game messages
    intro db "Instructions:", 0xA, "Think of a whole number in the range of 1 to 5000 and I will guess it!", 0xA
    introLen equ $-intro
    YES db "Your answer is Yes!", 0xA, 0xA
    yesLen equ $-YES
    NO db "Your answer is No!", 0xA, 0xA
    noLen equ $-NO
    ERR db "NOT A VALID OPTION!", 0xA
    errLen equ $-ERR
    end db "I guessed the number!", 0xA, "Number: "
    endLen equ $-end
    att db "Attempts: "
    attLen equ $-att
    newLine db 0xA

    ;;; Question
    low db "Is your number lower than: "
    lowLen equ $-low
    high db "Is your number higher than: "
    highLen equ $-high
    isNumb db "Is your number: "
    isNumbLen equ $-isNumb
    yn db "(Y)es or (N)o? : "
    ynLen equ $-yn

    ;;; Counter variables
    buffer  db '0000'
    zero    db '0000'
    one     db '0001'
    two     db '0002'
    five    db '0005'
    ten     db '0010'
    twenty  db '0020'
    fifty   db '0050'
    hundred db '0100'

section .bss
    answer_buf  resw 4 ;;; Answers
    count       resw 4 ;;; Number of questions
    borderL     resw 4 ;;; Lower possible number
    borderH     resw 4 ;;; Higher possible number
    guess       resw 4 ;;; Given guess
    buff        resw 4 ;;; Buffer

;;; Program section
section .text
    global _start
_start: ;;;Tell linker entry point
    jmp Main ;;;Making sure we start from main!

;;; Main function
Main:
    ;;; Setting counter and border to 0 and guess to 10
    mov ebx, '0000'
    mov [count], ebx
    mov ebx, '0000'
    mov [borderL], ebx
    mov ebx, '5000'
    mov [borderH], ebx
    mov ebx, '0100'
    mov [guess], ebx

    ;;; Print instructions
    mov ecx, intro
    mov edx, introLen
    call cout
    
    ;;; Start Game
    call guessNum

    ;;; Print Game stats
    mov ecx, end
    mov edx, endLen
    call cout
    mov ecx, guess
    mov edx, 4
    call cout

    mov ecx, newLine
    mov edx, 1
    call cout

    mov ecx, att
    mov edx, attLen
    call cout
    mov ecx, count
    mov edx, 4
    call cout
    
    ;;;Exit Game
    call exit

;;;  Guess the number function
;;;  -- Geting the user input
;;;  -- The function cicles untill it guesses the correct number
;;;  Is Higher Than |Yes| -- |No|
;;;^          ^_______|        |  ^
;;;|             _____________|   |
;;;| Is Lower Than |Yes| -- |No|  |
;;;\_________________|        |   |
;;;          ________________|    |
;;;  Is Number    |Yes| -- |No|---|
;;;              |Exit|
guessNum:
    mov eax, [guess]
    mov [buff], eax
    jmp HIGHER

    HIGHER:
    call counter
    mov ecx, high
    mov edx, highLen
    call cout
    mov ecx, guess
    mov edx, 4
    call cout
    mov ecx, newLine
    mov edx, 1
    call cout
    call input
    mov ecx, [answer_buf]
    cmp ecx, 1
    je HY ;;; In case the answer is YES
    cmp ecx, 0
    je HN ;;; In case the answer is NO

    LOWER:
    call counter
    mov ecx, low
    mov edx, lowLen
    call cout
    mov ecx, guess
    mov edx, 4
    call cout
    mov ecx, newLine
    mov edx, 1
    call cout
    call input
    mov ecx, [answer_buf]
    cmp ecx, 1
    je LY ;;; In case the answer is YES
    cmp ecx, 0
    je LN ;;; In case the answer is NO

    IS:
    call counter
    mov ecx, isNumb
    mov edx, isNumbLen
    call cout
    mov ecx, guess
    mov edx, 4
    call cout
    mov ecx, newLine
    mov edx, 1
    call cout
    call input
    mov ecx, [answer_buf]
    cmp ecx, 1
    je IY ;;; In case the answer is YES
    cmp ecx, 0
    je IN ;;; In case the answer is NO

    HY: ;;; In case the answer is YES
    mov eax, [guess]
    mov [borderL], eax
    call reduce_buffer
    mov edi, guess
    mov ebx, buff
    call ADD
    mov edi, [buffer]
    mov [guess], edi
    call guessCheck
    jmp HIGHER

    HN: ;;; In case the answer is NO
    mov eax, [guess]
    mov [borderH], eax
    call reduce_buffer
    mov edi, guess
    mov ebx, buff
    call SUB
    mov edi, [buffer]
    mov [guess], edi
    call guessCheck
    jmp LOWER

    LY: ;;; In case the answer is YES
    call guessCheck
    mov eax, [guess]
    mov [borderH], eax
    call reduce_buffer
    mov edi, guess
    mov ebx, buff
    call SUB
    mov edi, [buffer]
    mov [guess], edi
    jmp HIGHER

    LN: ;;; In case the answer is NO
    mov eax, [guess]
    mov [borderL], eax
    call reduce_buffer
    mov edi, guess
    mov ebx, buff
    call ADD
    mov edi, [buffer]
    mov [guess], edi
    call guessCheck
    jmp IS

    IY: ;;; In case the answer is YES
    ret

    IN: ;;; In case the answer is NO
    call reduce_buffer
    mov ebx, [buff]
    cmp [one], ebx
    jne JO ;;; Making sure not get stuck on one number
    mov edi, guess
    mov ebx, buff
    call SUB
    mov edi, [buffer]
    mov [guess], edi
    call guessCheck
    JO:
    jmp HIGHER

;;; Changing the number by which the guess is reduces
reduce_buffer:
    mov edi, borderH
    mov ebx, borderL
    call SUB
    mov edi, [buffer]

    cmp [two], edi
    je minOne ;;; Reduces the guess reduction from 2 to 1
    cmp [five], edi
    je minTwo ;;; Reduces the guess reduction from 5 to 2
    cmp [ten], edi
    je minFive ;;; Reduces the guess reduction from 10 to 5
    cmp [twenty], edi
    je minTen ;;; Reduces the guess reduction from 20 to 10
    cmp [fifty], edi
    je minTwenty ;;; Reduces the guess reduction from 50 to 20
    cmp [hundred], edi
    je minFifty ;;; Reduces the guess reduction from 100 to 50
    ret

    minFifty:
    mov eax, [fifty]
    mov [buff], eax
    ret

    minTwenty:
    mov eax, [twenty]
    mov [buff], eax
    ret

    minTen:    
    mov eax, [ten]
    mov [buff], eax
    ret

    minFive:
    mov eax, [five]
    mov [buff], eax
    ret

    minTwo:
    mov eax, [two]
    mov [buff], eax
    ret

    minOne:
    mov eax, [one]
    mov [buff], eax
    ret

;;; Checking if the guess is under 0 (prevent illigall values)
guessCheck:
    mov edi, zero
    mov ebx, one
    call SUB
    mov ecx, [guess]
    cmp ecx, [buffer]
    jnge LH
    mov eax, [zero]
    mov [guess], eax
    LH: ret

;;; User input function
input:
    mov eax, 0              ;\Making sure the
    mov [answer_buf], eax   ;/variable is empty

    mov ecx, yn
    mov edx, ynLen
    call cout

    mov ecx, answer_buf ;;; Store data in answer_buf
    mov edx, 32 ;;; Moving 32 bytes to make sure nothing is overwriten
    call cin

    mov ecx, [answer_buf]
    sub ecx, 0xa00 ;;; Removing the \n from the input

    ;;; Checking for the correct input
    cmp ecx, 'y'
    je yes
    cmp ecx, 'Y'
    je yes
    cmp ecx, 'n'
    je no
    cmp ecx, 'N'
    je no

    mov ecx,ERR
    mov edx,errLen
    call cout
    loop input

    yes:
    mov ecx, 1
    mov [answer_buf], ecx
    mov ecx,YES
    mov edx,yesLen
    jmp out

    no:
    mov ecx, 0
    mov [answer_buf], ecx
    mov ecx,NO
    mov edx,noLen
    jmp out

    out:
    call cout
    ret

;;; Counter function
counter:
    mov edi, count
    mov ebx, one
    call ADD
    mov edi, [buffer]
    mov [count], edi
    ret

;;; Addition function
ADD:
    mov esi, 3 ;;; Pointing to the rightmost digit
    mov ecx, 4 ;;; Num of digits
    clc
    add_loop:
        mov al, [edi + esi]
        adc al, [ebx + esi] ;;; Adding with carry
        aaa
        pushf
        xor al, 30h
        popf
        mov	[buffer + esi], al ;;; Save value in buffer value
        dec	esi
    loop add_loop
    ret

;;; Subtraction function
SUB:
    mov esi, 3 ;;; Pointing to the rightmost digit
    mov ecx, 4 ;;; Num of digits
    clc
    sub_loop:
        mov al, [edi + esi]
        sbb al, [ebx + esi] ;;; Subtracting with carry
        aas
        pushf
        xor al, 30h
        popf
        mov	[buffer + esi], al ;;; Save value in buffer value
        dec	esi
    loop sub_loop
    ret

;;; Output function
cout:
    mov eax,SYS_WRITE
    mov ebx,STDOUT
    int 80h
    ret

;;; Input function
cin:
    mov eax,SYS_READ
    mov ebx,STDIN
    int 80h
    ret

;;; Exit function
exit:
    mov eax,SYS_EXIT
    xor ebx,ebx
    int 80h