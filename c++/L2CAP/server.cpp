#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <bluetooth/bluetooth.h>
#include <bluetooth/l2cap.h>

int main(int argc, char **argv)
{
    struct sockaddr_l2 loc_addr = {0}, rem_addr = {0};
    char buf[1024] = {0};
    int s, client, bytes_read;
    socklen_t opt = sizeof(rem_addr);

    // allocate socket
    s = socket(AF_BLUETOOTH, SOCK_SEQPACKET, BTPROTO_L2CAP);

    bdaddr_t bdaddr_any =  {{0, 0, 0, 0, 0, 0}};
    loc_addr.l2_family = AF_BLUETOOTH;
    loc_addr.l2_bdaddr = bdaddr_any;
    loc_addr.l2_psm = htobs(0x1001);

    // bind socket to port 0x1001 of the first available
    bind(s, (struct sockaddr *)&loc_addr, sizeof(loc_addr));

    // put socket into listening mode
    listen(s, 1);

    // accept one connection
    client = accept(s, (struct sockaddr *)&rem_addr, &opt);

    // converting bluetooth device address -> string
    ba2str( &rem_addr.l2_bdaddr, buf );
    
    // buf = client address 
    fprintf(stderr, "accepted connection from %s\n", buf);

    memset(buf, 0, sizeof(buf));

    // read data from the client
    bytes_read = read(client, buf, sizeof(buf));

    if( bytes_read > 0 ) {
        printf("received [%s]\n", buf);
    }

    // close connection
    close(client);
    
    // close socket
    close(s);
}