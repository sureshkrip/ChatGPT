      01  HACKATHON-X.     
           08  HACKATHON-WK. 
      ***START OF KEY*** 		   
           10  HEADER_KEY.                                                          
               15  CUSTOMER-NO             PIC XXXXXXX.                             
               15  AUTO-NO.                                                     
                   17  AUTO-NO             PIC X(9).                            
                   17  AUTO-CK-DIG         PIC X.                               
               15  AUTO-NO-P20 REDEFINES AUTO-NO                                
                                           PIC 9(20) COMP-3.   
      ***END OF KEY*** 										   
           10  BANK-DETAILS.                                                      
               15  BANK-INV-CODE.                                                    
                   17  BANK-NO             PIC XXX.                        
                   17  BANK-LOAN-NO        PIC X(10).                           
                   17  BANK-LOAN-NO-RJ REDEFINES BANK-LOAN-NO               
                                           PIC X(10)       JUST RIGHT.          
               15  DOLLAR-BALS             COMP-3.              
                   17  ORIGINAL-BAL        PIC S9(9)V99.                        
                   17  PAYOFF-BAL          PIC S9(9)V99.                        
               15  PAYMT-TERMS.                                          
                   17  ANNUAL-INT          PIC SV9(7)      COMP-3.              
                   17  INTEREST-RATE REDEFINES ANNUAL-INT                       
                                           PIC S99V9(5)    COMP-3.              
               15  DATES.                                                 
                   17  DUE-DATE.                                                
                       19  DUE-YR-MO.                                           
                           21  DUE-YR      PIC 999 COMP-3.                      
                           21  DUE-MO      PIC 99.                              
                       19  DUE-DA          PIC 99.                           
               15  CAR-OPTIONS-SWITCHES    PIC X(15).                          
               15  CAR-OPTIONSX REDEFINES  CAR-OPTIONS-SWITCHES.                  
                   17  CAR-OPTIONS-CHAR    PIC X  OCCURS 15 TIMES.                        
                                  