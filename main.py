from getData import gemini_response 

def handle_status_codes(response, addr):
    status_code = response[0:2]
    first_digit = status_code[0]
    second_digit = status_code[1]
    #have to separate response header and response body
    header_end = 0
    while(response[header_end] != "\n"):
        header_end +=1
    response_header = response[0:header_end + 1]
    response_body = response[header_end+1 : len(response)]
    match first_digit:
        case "1":
            theInput = input(response_body + "\n")
            quesPos = 0
            while(addr[quesPos] != "?"):
                quesPos += 1
            queryResponse = addr[0:quesPos + 1] + theInput
            #will need to create a more rigorous form of sending data to enable this to work well.
            return(queryResponse)
        case "2":
            print(response_body)
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass


dns_addr = "gemini.jaccident.co.uk"
theResponse = gemini_response(dns_addr)
handle_status_codes(theResponse, dns_addr)
