
"""
                                                        
                          **      *                     
  *                        **   **                      
 ***                       **   **                      
  *                        **   **                      
                           **   **        **   ****     
***     ***  ****      *** **   **  ***    **    ***  * 
 ***     **** **** *  ********* ** * ***   **     ****  
  **      **   ****  **   ****  ***   ***  **      **   
  **      **    **   **    **   **     **  **      **   
  **      **    **   **    **   **     **  **      **   
  **      **    **   **    **   **     **  **      **   
  **      **    **   **    **   **     **  **      **   
  **      **    **   **    **   **     **   ******* **  
  *** *   ***   ***   *****     **     **    *****   ** 
   ***     ***   ***   ***       **    **               
                                       *                
                                      *                 
                                     *                  
                                    *                   
                                                        
"""

for _ in range(int(input())):
    s=input()
    n=len(s)
    if len(s)==1:
        print("Yes")
        continue
    t1=True
    s1=s[0]
    for i in range(0,n,2):

        if s[i]!=s1:
            t1=False
            break
    t2=True
    s2=s[1]
    for i in range(1,n,2):

        if s[i]!=s2:
            t2=False
            break
    if t1 and t2:
        print("Yes")
    else:
        print("No")