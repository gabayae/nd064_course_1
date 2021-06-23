

In solving Exercise 03, the following error appeared:
                         
                         
                      >[4/4] RUN go build -o helloworld:
                    #9 0.233  go: go.mod file not found in current directory or any parent directory; see 'go help modules'
                    
                    
To fix it, I ran
                     
                                go mod init main.go
                                
                          
 Alternatively, I believde this can be fixed by adding in my Dockerfile the following lines
 
                                      COPY go.mod .
                                      COPY go.sum .
                                      RUN go mod download
