# (c) 2021 Davide Gaffoglio
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import random

# GENERO NUMERI CASUALI E VEDO DOPO QUANTO TEMPO LA SEQUENZA DI LUNGHEZZA N SI RIPETE
MIN_RANDOM = 0
MAX_RANDOM = 100


def sublist_in_list(lenSeq, l, sl) -> bool:
    retVal = False
    for i in range(lenSeq - 1, len(l)):
        csl = l[i - (lenSeq - 1):(i + 1)]
        if csl == sl:
            retVal = True
            break
    return retVal


def exercise(lenSeq):
    random.seed(42)
    retVal = []
    while True:
        r = random.randint(MIN_RANDOM, MAX_RANDOM)
        retVal.append(r)
        if len(retVal) >= (lenSeq * 2) and sublist_in_list(lenSeq, retVal[:(lenSeq * -1)],
                                                           retVal[lenSeq * -1:]):
            break
    return retVal


def main():
    lenSeq = int(input('Lunghezza sequenza: '))
    lista = exercise(lenSeq)
    print(f'Una sequenza lunga {lenSeq} si ripete ogni {len(lista)} generazioni')
    sequenza = []
    for i in range(lenSeq):
        sequenza.append(lista[(lenSeq - i) * -1])
    print(sequenza)


if __name__ == '__main__':
    main()
