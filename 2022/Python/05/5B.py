import string
import re
class SupStack:
    def __init__(self) -> None:
        self.raw_data = []
        self.map = []
        self.inst = []

    def main(self):

        # Quick rules for reformatting:
        # str len should be cols * 3
        # cols -1 = extra whitespace
        # Cranes can only move one at a time
        print("Reading data")
        self.read_data()
        print("Splitting data into two subtypes:")
        # fmt = self.raw_data.strip()
        a, b = self.raw_data.split("\n\n")

        fa = a.split("\n")
        # print(len(fa[0]))
        char_range = range(1,  len(fa[0]) , 4)
        height = range(0,len(fa)-1)
        print(f'Height: {height}')

        updated_map = []
        for n in char_range:
            #Go across for each item
            col = []
            for y_pos in height:
                # print(fa[y_pos][n])
                current_char = fa[y_pos][n]
                if(current_char != ' '):
                    col.append(current_char)
            self.map.append(col)
        
        print(self.map)
        
        # ----- INST TIME
        fb = b.split("\n")
        # [0] - count
        # [1] - From
        # [2] - To

        tmp = []
        for line in fb:
            tmp.append(re.sub(r'[a-z]','', line.lower()))
        for line in tmp:
            self.inst.append(line.split( )[0:])
        
        print("Instructions:")
        print(self.inst)
        # For Part2, moving doesnt work the same as pop

        for instruction in self.inst:
            max_count = int(instruction[0])
            from_adr = int(instruction[1]) -1
            to_adr = int(instruction[2]) -1

            counter = 0
            # Get vals we want to move first
            # Could be like we have them picked up
            held_boxes = []
            while counter < max_count:
                held_boxes.append(self.map[from_adr][0])
                self.map[from_adr].pop(0)
                counter += 1
            held_boxes.reverse()
            print(f'Holding: {held_boxes}')
            for box in held_boxes:
                self.map[to_adr].insert(0, box)

        print(self.map)

        message = ""
        for col in self.map:
            message += col[0]
            # print(col[0], end="")
        print(message)
        
        
    def read_data(self):
        f = open("dataset.txt", "r")
        self.raw_data = f.read()


if __name__== '__main__':
    SupStack().main()