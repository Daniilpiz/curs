includelib kernel32.lib   ; подключаем библиотеку kernel32.lib

; подключаем функции WriteFile и GetStdHandle
extrn WriteFile: PROC
extrn GetStdHandle: PROC
.code
indent byte "    ", 0  ; Отступ (4 пробела)
text byte "Coursework on the topic of solving matrix equations by the inverse matrix method", 0    ; выводимая строка

main proc
  sub  rsp, 40   ; Для параметров функций WriteFile и GetStdHandle резервируем 40 байт (5 параметров по 8 байт)

  ; Вывод отступа (дважды)
  mov  rcx, -11  ; Аргумент для GetStdHandle - STD_OUTPUT
  call GetStdHandle
  mov  rcx, rax
  lea  rdx, indent
  mov  r8d, 4      ; Длина отступа (4 пробела)
  xor  r9, r9
  mov  qword ptr [rsp + 32], 0
  call WriteFile

  ; Повторный вывод отступа
  mov  rcx, rax
  lea  rdx, indent
  mov  r8d, 4      ; Длина отступа (4 пробела)
  xor  r9, r9
  mov  qword ptr [rsp + 32], 0
  call WriteFile

  mov  rcx, rax
  lea  rdx, indent
  mov  r8d, 4      ; Длина отступа (4 пробела)
  xor  r9, r9
  mov  qword ptr [rsp + 32], 0
  call WriteFile

  ; Вывод текста
  mov  rcx, -11  ; Аргумент для GetStdHandle - STD_OUTPUT
  call GetStdHandle ; вызываем функцию GetStdHandle
  mov  rcx, rax     ; Первый параметр WriteFile - в регистр RCX помещаем дескриптор файла - консоли
  lea  rdx, text    ; Второй параметр WriteFile - загружаем указатель на строку в регистр RDX
  mov  r8d, 80      ; Третий параметр WriteFile - длина строки для записи в регистре R8D
  xor  r9, r9       ; Четвертый параметр WriteFile - адрес для получения записанных байтов
  mov  qword ptr [rsp + 32], 0  ; Пятый параметр WriteFile
  call WriteFile ; вызываем функцию WriteFile

  add  rsp, 40
  ret
main endp
end
