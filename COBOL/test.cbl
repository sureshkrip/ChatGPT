       IDENTIFICATION DIVISION. 
       PROGRAM-ID. HELLO.
       DATA DIVISION. 
       WORKING-STORAGE SECTION. 
           01 COUNTER PIC 9(3).
           01 SOURCE PIC X(80) VALUE 'HELLO WORLD'.
                 
       PROCEDURE DIVISION.
           DISPLAY 'Hello World'.
           MOVE 0 to COUNTER
           INSPECT SOURCE TALLYING COUNTER FOR ALL SPACES
           STOP RUN.

