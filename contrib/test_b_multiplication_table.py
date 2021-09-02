# Written by Eric Orso
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

##  @package multiplication table
#ask for a number
#print the multiplication table for theat number
#square

#ask user for number
user_str = input('Gimme NUMBER!')
user_num = int(user_str)
assert(user_num >0), f"... DVMMY!"
#activate header
u1_header = True
#scan mul factors on rows
for num_row in range(1, user_num+1 +1):

    #if print header mode
    if u1_header == True:
        print(f" \t",end='')
    #if print row header
    else:
        #print row header
        print(f"{(num_row-1)}\t",end='')
    
    #scan mul factors on cols
    for num_col in range(1, user_num+1):
        if u1_header == True:
            print(f"| {(num_col)}\t",end='')
        else:
            #print row header
            print(f"| {(num_row-1) *(num_col)}\t",end='')
            
    #deactivate header mode
    u1_header = False

    #end row
    print("|")
