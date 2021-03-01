from namedlist import namedlist
import math

pc=0
cycle=0

####################################################### Issue ####################################################

def find_rs_space(rs):                                  # Finding empty space in the given rs/buffer and returning its index
    index=-1
    for i in range(len(rs)):
        if(rs[i].busy==0):
            index=i
            break
    return index

def put_instruction_into_rs(rs1,index,ins,reg):       # putting instruction into rs
    rs=rs1[index]
    rs.busy=1
    rs.opcode=ins.split(' ')[0]


    '''dest=ins.split(' ')[1][1:]
    reg[int(dest)].busy=1
    reg[int(dest)].tag=rs.rs_tag'''

    src1=ins.split(' ')[2][1:]
    if(reg[int(src1)].busy==0):
        rs.tag1=0
        rs.value1=reg[int(src1)].data
    elif(reg[int(src1)].busy==1):
        rs.tag1=reg[int(src1)].tag

    try:
        src2=ins.split(' ')[3][1:]
        if(reg[int(src2)].busy==0):
            rs.tag2=0
            rs.value2=reg[int(src2)].data
        elif(reg[int(src2)].busy==1):
            rs.tag2=reg[int(src2)].tag
    except:
        pass

    dest=ins.split(' ')[1][1:]
    reg[int(dest)].busy=1
    reg[int(dest)].tag=rs.rs_tag

def put_instruction_into_buffer(buffer1,index,ins,reg):    # putting instruction into buffer
    buf=buffer1[index]
    buf.busy=1
    buf.opcode=ins.split(' ')[0]
    buf.address=ins.split(' ')[2]

    if(buf.opcode=="LDR"):
        dest=ins.split(' ')[1][1:]
        reg[int(dest)].busy=1
        reg[int(dest)].tag=buf.ldst_tag
    else:
        src=ins.split(' ')[1][1:]
        if(reg[int(src)].busy):
            buf.tag=reg[int(src)].tag
        else:
            buf.value=reg[int(src)].data
            buf.tag=0

# issuing instruction from instructions_queue
def issue(instructions_queue,int_add_rs,int_mul_rs,float_add_rs,float_mul_rs,shift_rs,comp_rs,nand_rs,xor_rs,ldst_buffer,int_register,fp_register):
    global pc
    ins=instructions_queue[pc]
    print(ins)
    op=ins.split(' ')[0]
    if(op=="LDR"):
        flag=0
        for i in range (4):
            if(ldst_buffer[i].busy==1 and ldst_buffer[i].opcode=="STR" and ldst_buffer[i].address==ins.split(' ')[2]):
                flag=1
                break
        if (flag==0):
            index=find_rs_space(ldst_buffer)
            if(index!=-1):
                if (ins.split(' ')[1][:1]=='R' or ins.split(' ')[1][:1]=='r'):
                    put_instruction_into_buffer(ldst_buffer,index,ins,int_register)
                else:
                    put_instruction_into_buffer(ldst_buffer,index,ins,fp_register)
                pc+=1

    elif(op=="STR"):
        flag=0
        for i in range (4):
            if(ldst_buffer[i].busy==1 and ldst_buffer[i].address==ins.split(' ')[2]):
                flag=1
                break
        if (flag==0):
            index=find_rs_space(ldst_buffer)
            if(index!=-1):
                if (ins.split(' ')[1][:1]=='R' or ins.split(' ')[1][:1]=='r'):
                    put_instruction_into_buffer(ldst_buffer,index,ins,int_register)
                else:
                    put_instruction_into_buffer(ldst_buffer,index,ins,fp_register)
                pc+=1

    elif(op=="ADD" or op=="ADC" or op=="SUB" or op=="SBB"):
        index=find_rs_space(int_add_rs)
        if(index!=-1):
            put_instruction_into_rs(int_add_rs,index,ins,int_register)
            pc=pc+1

    elif(op=="FADD" or op=="FSUB"):
        index=find_rs_space(float_add_rs)
        if(index!=-1):
            put_instruction_into_rs(float_add_rs,index,ins,fp_register)
            pc=pc+1

    elif(op=="MUL"):
        index=find_rs_space(int_mul_rs)
        if(index!=-1):
            put_instruction_into_rs(int_mul_rs,index,ins,int_register)
            pc=pc+1

    elif(op=="FMUL"):
        index=find_rs_space(float_mul_rs)
        if(index!=-1):
            put_instruction_into_rs(float_mul_rs,index,ins,fp_register)
            pc=pc+1

    elif(op=="XOR"):
        index=find_rs_space(xor_rs)
        if(index!=-1):
            put_instruction_into_rs(xor_rs,index,ins,int_register)
            pc=pc+1

    elif(op=="NAND"):
        index=find_rs_space(nand_rs)
        if(index!=-1):
            put_instruction_into_rs(nand_rs,index,ins,int_register)
            pc=pc+1

    elif(op=="LHR" or op=="SHR"):
        index=find_rs_space(shift_rs)
        if(index!=-1):
            put_instruction_into_rs(shift_rs,index,ins,int_register)
            pc=pc+1

    elif(op=="CMP"):
        index=find_rs_space(comp_rs)
        if(index!=-1):
            put_instruction_into_rs(comp_rs,index,ins,int_register)
            pc=pc+1

    elif(op=="HLT"):
        pc=-1

#################################################### Issue End ###########################################################


################################################ Execute ###############################################

# maintaining the pipelines of functional units
def exe_pipeline(fu,index,fu_name):
    print("------------#######------------",fu[0].cnt,fu[1].cnt,fu[2].cnt)

    filename="output/"+fu_name+"/"+fu_name+"@"+str(cycle)+".txt"
    f=open(filename,"w")
    s=str(fu[0].cnt)+" "+str(fu[1].cnt)+" "+str(fu[2].cnt)+"\n"
    f.write(s)
    f.close()


    if(fu[2].busy==1):
        fu[2].cnt+=1
        if(fu[2].cnt>fu[2].cycle and result_buffer[index].busy==0):
            fu[2].busy=0
            result_buffer[index].busy=1
            result_buffer[index].tag=fu[2].rs_tag
            fu[2].cnt=0
            if(fu[2].opcode=="ADD"):
                result_buffer[index].result=fu[2].value1+fu[2].value2
            elif(fu[2].opcode=="ADC"):
                result_buffer[index].result=fu[2].value1+fu[2].value2+1                ## assuming carry flag is set
            elif(fu[2].opcode=="SUB"):
                result_buffer[index].result=fu[2].value1-fu[2].value2
            elif(fu[2].opcode=="SBB"):
                result_buffer[index].result=fu[2].value1-fu[2].value2-1
            elif(fu[2].opcode=="MUL"):
                result_buffer[index].result=fu[2].value1*fu[2].value2
            elif(fu[2].opcode=="FADD"):
                result_buffer[index].result=fu[2].value1+fu[2].value2
            elif(fu[2].opcode=="FSUB"):
                result_buffer[index].result=fu[2].value1-fu[2].value2
            elif(fu[2].opcode=="FMUL"):
                result_buffer[index].result=fu[2].value1*fu[2].value2
            elif(fu[2].opcode=="CMP"):
                result_buffer[index].result=~(fu[2].value1)
            elif(fu[2].opcode=="NAND"):
                result_buffer[index].result=~(fu[2].value1 & fu[2].value2)
            elif(fu[2].opcode=="XOR"):
                result_buffer[index].result=(fu[2].value1 ^ fu[2].value2)
            elif(fu[2].opcode=="LHR"):
                result_buffer[index].result=(fu[2].value1)<<fu[2].value2
            elif(fu[2].opcode=="SHR"):
                result_buffer[index].result=(fu[2].value1)>>fu[2].value2


    if(fu[1].busy==1):
        fu[1].cnt+=1
        if(fu[1].cnt>fu[1].cycle and fu[2].busy==0):
            fu[1].cnt=0
            fu[1].busy=0
            fu[2].busy=1
            fu[2].cnt+=1
            fu[2].rs_tag=fu[1].rs_tag
            fu[2].opcode=fu[1].opcode
            fu[2].value1=fu[1].value1
            fu[2].value2=fu[1].value2

    if(fu[0].busy==1):
        fu[0].cnt+=1
        if(fu[0].cnt>fu[0].cycle and fu[1].busy==0):
            fu[0].cnt=0
            fu[0].busy=0
            fu[1].busy=1
            fu[1].cnt+=1
            fu[1].rs_tag=fu[0].rs_tag
            fu[1].opcode=fu[0].opcode
            fu[1].value1=fu[0].value1
            fu[1].value2=fu[0].value2

# Fetching instruction from RS which are ready to execute in FU
def exe_fetch(fu,rs):
    if(fu[0].busy==0 and rs.issued==0):
        fu[0].cnt+=1
        fu[0].busy=1
        fu[0].rs_tag=rs.rs_tag
        fu[0].opcode=rs.opcode
        fu[0].value1=rs.value1
        fu[0].value2=rs.value2
        rs.issued=1

# maintaining pipelines of Load/Store FU
def ldst_exe_pipeline(fu,fu_name):
    print("-----------------",fu[0].cnt,fu[1].cnt,fu[2].cnt)

    filename="output/"+fu_name+"/"+fu_name+"@"+str(cycle)+".txt"
    f=open(filename,"w")
    s=str(fu[0].cnt)+" "+str(fu[1].cnt)+" "+str(fu[2].cnt)+"\n"
    f.write(s)
    f.close()



    if(fu[2].busy==1):
        fu[2].cnt+=1
        if(fu[2].cnt>fu[2].cycle and result_buffer[0].busy==0):
            fu[2].busy=0
            result_buffer[0].busy=1
            fu[2].cnt=0
            if(fu[2].opcode=="LDR"):
                result_buffer[0].result=int(memory[int(fu[2].address)])
                result_buffer[0].tag=fu[2].ldst_tag
            elif(fu[2].opcode=="STR"):
                result_buffer[0].address=fu[2].address
                result_buffer[0].result=fu[2].value
                result_buffer[0].tag=fu[2].ldst_tag


    if(fu[1].busy==1):
        fu[1].cnt+=1
        if(fu[1].cnt>fu[1].cycle and fu[2].busy==0):
            fu[1].cnt=0
            fu[1].busy=0
            fu[2].busy=1
            fu[2].cnt+=1
            fu[2].ldst_tag=fu[1].ldst_tag
            fu[2].opcode=fu[1].opcode
            fu[2].value=fu[1].value
            fu[2].address=fu[1].address

    if(fu[0].busy==1):
        fu[0].cnt+=1
        if(fu[0].cnt>fu[0].cycle and fu[1].busy==0):
            fu[0].cnt=0
            fu[0].busy=0
            fu[1].busy=1
            fu[1].cnt+=1
            fu[1].ldst_tag=fu[0].ldst_tag
            fu[1].opcode=fu[0].opcode
            fu[1].value=fu[0].value
            fu[1].address=fu[0].address

# Fetching load/store instruction from load/store buffer which are ready to execute in FU
def ldst_exe_fetch(fu,buf):
    if(fu[0].busy==0 and buf.issued==0):
        fu[0].cnt+=1
        fu[0].busy=1
        fu[0].ldst_tag=buf.ldst_tag
        fu[0].opcode=buf.opcode
        fu[0].value=buf.value
        fu[0].address=buf.address
        buf.issued=1

# Execute stage of tomasulo
def execute(instructions_queue,int_add_rs,int_mul_rs,float_add_rs,float_mul_rs,shift_rs,comp_rs,nand_rs,ldst_buffer,xor_rs,int_add_fu,int_mul_fu,float_add_fu,float_mul_fu,shift_fu,comp_fu,nand_fu,xor_fu,ldst_fu):
    for i in range(3):
        if(int_add_rs[i].tag1==0 and int_add_rs[i].tag2==0 and int_add_rs[i].busy==1):
            exe_fetch(int_add_fu,int_add_rs[i])

        if(int_mul_rs[i].tag1==0 and int_mul_rs[i].tag2==0 and int_mul_rs[i].busy==1):
            exe_fetch(int_mul_fu,int_mul_rs[i])

        if(float_add_rs[i].tag1==0 and float_add_rs[i].tag2==0 and float_add_rs[i].busy==1):
            exe_fetch(float_add_fu,float_add_rs[i])

        if(float_mul_rs[i].tag1==0 and float_mul_rs[i].tag2==0 and float_mul_rs[i].busy==1):
            exe_fetch(float_mul_fu,float_mul_rs[i])

        if(shift_rs[i].tag1==0 and shift_rs[i].tag2==0 and shift_rs[i].busy==1):
            exe_fetch(shift_fu,shift_rs[i])

    for i in range(2):
        if(nand_rs[i].tag1==0 and nand_rs[i].tag2==0 and nand_rs[i].busy==1):
            exe_fetch(nand_fu,nand_rs[i])

        if(xor_rs[i].tag1==0 and xor_rs[i].tag2==0 and xor_rs[i].busy==1):
            exe_fetch(xor_fu,xor_rs[i])

        if(comp_rs[i].tag1==0 and comp_rs[i].busy==1):
            exe_fetch(comp_fu,comp_rs[i])

    for i in range(4):
        if(ldst_buffer[i].busy==1):
            if((ldst_buffer[i].opcode=="STR" and ldst_buffer[i].tag==0) or (ldst_buffer[i].opcode=="LDR")):
                ldst_exe_fetch(ldst_fu,ldst_buffer[i])

    exe_pipeline(int_add_fu,4,"int_add_fu")
    exe_pipeline(int_mul_fu,3,"int_mul_fu")
    exe_pipeline(float_add_fu,2,"float_add_fu")
    exe_pipeline(float_mul_fu,1,"float_mul_fu")
    exe_pipeline(shift_fu,5,"shift_fu")
    exe_pipeline(nand_fu,8,"nand_fu")
    exe_pipeline(xor_fu,7,"xor_fu")
    exe_pipeline(comp_fu,6,"comp_fu")
    ldst_exe_pipeline(ldst_fu,"ldst_fu")


################################################### Execute end ###################################################

################################################## Write result ##################################################
def pop_rs(rs):              # popping completed/executed instruction from rs
    rs.busy=0
    rs.issued=0
    rs.opcode="XXX"
    rs.tag1=-1
    rs.tag2=-1
    rs.value1=math.inf
    rs.value2=math.inf

# write result stage of Tomasulo
def write_result(int_add_rs,int_mul_rs,float_add_rs,float_mul_rs,shift_rs,comp_rs,nand_rs,ldst_buffer,xor_rs,int_register,fp_register,int_add_fu,int_mul_fu,float_add_fu,float_mul_fu,shift_fu,comp_fu,nand_fu,xor_fu,ldst_fu):
    # global cdb
    for i in range(9):
        if(cdb.busy==0):
            if(result_buffer[i].busy==1):
                if(i==0 and result_buffer[i].address!=-1): #store
                    memory[int(result_buffer[i].address)]=result_buffer[i].result
                    # file1 = open('memory.txt', 'w')
                    # for j in range(len(memory)):
                    #     file1.write(str(memory[j])+"\n")
                    # file1.close()

                    index=result_buffer[i].tag-22
                    ldst_buffer[index].busy=0
                    ldst_buffer[index].issued=0
                    ldst_buffer[index].opcode="XXX"
                    ldst_buffer[index].address=-1
                    ldst_buffer[index].tag=-1
                    ldst_buffer[index].value=math.inf
                else:
                    cdb.busy=1
                    cdb.result=result_buffer[i].result
                    cdb.tag=result_buffer[i].tag
                result_buffer[i].busy=0
                result_buffer[i].tag=-1
                result_buffer[i].result=math.inf
                result_buffer[i].address=-1
        else:
            break

    print("###################### CDB #####################")
    print(cdb.busy , cdb.tag , cdb.result)

    if(cdb.busy==1):
        for i in range(3):
            if(int_add_rs[i].tag1==cdb.tag and int_add_rs[i].busy==1):
                int_add_rs[i].value1=cdb.result
                int_add_rs[i].tag1=0

            if(int_add_rs[i].tag2==cdb.tag and int_add_rs[i].busy==1):
                int_add_rs[i].value2=cdb.result
                int_add_rs[i].tag2=0

            if(int_mul_rs[i].tag1==cdb.tag and int_mul_rs[i].busy==1):
                int_mul_rs[i].value1=cdb.result
                int_mul_rs[i].tag1=0

            if(int_mul_rs[i].tag2==cdb.tag and int_mul_rs[i].busy==1):
                int_mul_rs[i].value2=cdb.result
                int_mul_rs[i].tag2=0

            if(float_add_rs[i].tag1==cdb.tag and float_add_rs[i].busy==1):
                float_add_rs[i].value1=cdb.result
                float_add_rs[i].tag1=0

            if(float_add_rs[i].tag2==cdb.tag and float_add_rs[i].busy==1):
                float_add_rs[i].value2=cdb.result
                float_add_rs[i].tag2=0

            if(float_mul_rs[i].tag1==cdb.tag and float_mul_rs[i].busy==1):
                float_mul_rs[i].value1=cdb.result
                float_mul_rs[i].tag1=0

            if(float_mul_rs[i].tag2==cdb.tag and float_mul_rs[i].busy==1):
                float_mul_rs[i].value2=cdb.result
                float_mul_rs[i].tag2=0

            if(shift_rs[i].tag1==cdb.tag and shift_rs[i].busy==1):
                shift_rs[i].value1=cdb.result
                shift_rs[i].tag1=0

            if(shift_rs[i].tag2==cdb.tag and shift_rs[i].busy==1):
                shift_rs[i].value2=cdb.result
                shift_rs[i].tag2=0

        for i in range(2):
            if(nand_rs[i].tag1==cdb.tag and nand_rs[i].busy==1):
                nand_rs[i].value1=cdb.result
                nand_rs[i].tag1=0

            if(nand_rs[i].tag2==cdb.tag and nand_rs[i].busy==1):
                nand_rs[i].value2=cdb.result
                nand_rs[i].tag2=0

            if(xor_rs[i].tag1==cdb.tag and xor_rs[i].busy==1):
                xor_rs[i].value1=cdb.result
                xor_rs[i].tag1=0

            if(xor_rs[i].tag2==cdb.tag and xor_rs[i].busy==1):
                xor_rs[i].value2=cdb.result
                xor_rs[i].tag2=0

            if(comp_rs[i].tag1==cdb.tag and comp_rs[i].busy==1):
                comp_rs[i].value1=cdb.result
                comp_rs[i].tag1=0

        for i in range(4):
            if(ldst_buffer[i].busy==1):
                if(ldst_buffer[i].opcode=="STR" and ldst_buffer[i].tag==cdb.tag):
                    ldst_buffer[i].value=cdb.result
                    ldst_buffer[i].tag=0


        for i in range(16):
            if(int_register[i].busy==1 and int_register[i].tag==cdb.tag):
                int_register[i].data=cdb.result
                int_register[i].busy=0
                int_register[i].tag=0

            if(fp_register[i].busy==1 and fp_register[i].tag==cdb.tag):
                fp_register[i].data=cdb.result
                fp_register[i].busy=0
                fp_register[i].tag=0


        ###### pop out ins from rs #####
        if(cdb.tag<=3):  #1,2,3 for int_add_rs
            i=cdb.tag-1
            pop_rs(int_add_rs[i])
        elif(cdb.tag<=6):  #4,5,6 for int_mul_rs
            i=cdb.tag-4
            pop_rs(int_mul_rs[i])
        elif(cdb.tag<=9):  #7,8,9 for float_add_rs
            i=cdb.tag-7
            pop_rs(float_add_rs[i])
        elif(cdb.tag<=12):  #10,11,12 for float_mul_rs
            i=cdb.tag-10
            pop_rs(float_mul_rs[i])
        elif(cdb.tag<=15):  #13,14,15 for shift_rs
            i=cdb.tag-13
            pop_rs(shift_rs[i])
        elif(cdb.tag<=17):  #16,17 for comp_rs
            i=cdb.tag-16
            pop_rs(comp_rs[i])
        elif(cdb.tag<=19):  #18,19 for nand_rs
            i=cdb.tag-18
            pop_rs(nand_rs[i])
        elif(cdb.tag<=21):  #20,21 for xor_rs
            i=cdb.tag-20
            pop_rs(xor_rs[i])
        elif(cdb.tag<=25):  #22,23,24,25 for ldst_buffer
            i=cdb.tag-22
            ldst_buffer[i].busy=0
            ldst_buffer[i].tag=-1
            ldst_buffer[i].value=math.inf
            ldst_buffer[i].address=-1
            ldst_buffer[i].issued=0
            ldst_buffer[i].opcode="XXX"




################################################### Write result End ##################################################

# read instructions from instructions_queue
def read_instructions(instruction_file):
    with open(instruction_file) as file:
        instructions = file.read().splitlines()
    return instructions

def read_memory(memory_file):
    with open(memory_file) as file:
        mem = file.read().splitlines()
    return mem

# checking if given rs is empty
def is_empty(rs):
    for i in range(len(rs)):
        if(rs[i].busy==1):
            return 0
    return 1

################################################ int/float register initialization #####################################
def fp_register_entry():
    fp_register_entry = namedlist('fp_register_entry','busy tag data')
    temp=fp_register_entry
    return temp

def int_register_entry():
    int_register_entry = namedlist('int_register_entry','busy tag data')
    temp=int_register_entry
    return temp

fp_register = []
for _ in range(16):
    temp = fp_register_entry()
    temp.busy = 0
    temp.tag = -1               #tag -1 -> invalid
    temp.data = math.inf
    fp_register.extend([temp])

int_register = []
for _ in range(16):
    temp = int_register_entry()
    temp.busy = 0
    temp.tag = -1               #tag -1 -> invalid
    temp.data = math.inf
    int_register.extend([temp])
################################################ int/float register initialization End ##########################################



################################################# Reservation stations initialization ##########################################

def rs_entry():
    rs_entry = namedlist('rs_entry','rs_tag busy opcode tag1 value1 tag2 value2 issued')
    temp=rs_entry
    return temp

def ldst_entry():
    ldst_entry = namedlist('ldst_entry','ldst_tag busy opcode address tag value issued')
    temp=ldst_entry
    return temp

int_add_rs=[]
for i in range(3):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+1
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    int_add_rs.extend([temp])

int_mul_rs=[]
for i in range(3):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+4
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    int_mul_rs.extend([temp])

float_add_rs=[]
for i in range(3):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+7
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    float_add_rs.extend([temp])

float_mul_rs=[]
for i in range(3):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+10
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    float_mul_rs.extend([temp])

shift_rs=[]
for i in range(3):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+13
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    shift_rs.extend([temp])

comp_rs=[]
for i in range(2):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+16
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    comp_rs.extend([temp])

nand_rs=[]
for i in range(2):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+18
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    nand_rs.extend([temp])

xor_rs=[]
for i in range(2):
    temp=rs_entry()
    temp.busy=0
    temp.rs_tag=i+20
    temp.opcode="XXX"
    temp.tag1=-1
    temp.tag2=-1
    temp.value1=math.inf
    temp.value2=math.inf
    temp.issued=0
    xor_rs.extend([temp])

ldst_buffer=[]
for i in range(4):
    temp=ldst_entry()
    temp.busy=0
    temp.ldst_tag=ldst_tag=i+22
    temp.opcode="XXX"
    temp.address=-1
    temp.tag=-1
    temp.value=math.inf
    temp.issued=0
    ldst_buffer.extend([temp])

################################################# Reservation stations initialization End ##########################################



################################################### FU initialization #####################################################

def fu_entry():
    fu_entry=namedlist('fu_entry','busy rs_tag opcode value1 value2 cycle cnt')
    temp=fu_entry
    return temp

def ldst_fu_entry():
    ldst_fu_entry=namedlist('ldst_fu_entry','busy ldst_tag opcode address value cnt cycle')
    temp=ldst_fu_entry
    return temp

int_add_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    int_add_fu.extend([temp])
int_add_fu[0].cycle=1
int_add_fu[1].cycle=1
int_add_fu[2].cycle=6

int_mul_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    int_mul_fu.extend([temp])
int_mul_fu[0].cycle=1
int_mul_fu[1].cycle=1
int_mul_fu[2].cycle=11


float_add_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    float_add_fu.extend([temp])
float_add_fu[0].cycle=1
float_add_fu[1].cycle=1
float_add_fu[2].cycle=21

float_mul_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    float_mul_fu.extend([temp])
float_mul_fu[0].cycle=1
float_mul_fu[1].cycle=1
float_mul_fu[2].cycle=24

shift_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    shift_fu.extend([temp])
shift_fu[0].cycle=1
shift_fu[1].cycle=1
shift_fu[2].cycle=4

comp_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    comp_fu.extend([temp])
comp_fu[0].cycle=1
comp_fu[1].cycle=1
comp_fu[2].cycle=1

xor_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    xor_fu.extend([temp])
xor_fu[0].cycle=1
xor_fu[1].cycle=1
xor_fu[2].cycle=1

nand_fu = []
for i in range(3):
    temp=fu_entry()
    temp.busy=0
    temp.rs_tag=-1
    temp.opcode="XXX"
    temp.value1=math.inf
    temp.value2=math.inf
    temp.cnt=0
    nand_fu.extend([temp])
nand_fu[0].cycle=1
nand_fu[1].cycle=1
nand_fu[2].cycle=1

ldst_fu = []
for i in range(3):
    temp=ldst_fu_entry()
    temp.busy=0
    temp.ldst_tag=-1
    temp.address=-1
    temp.opcode="XXX"
    temp.value=math.inf
    temp.cnt=0
    ldst_fu.extend([temp])
ldst_fu[0].cycle=1
ldst_fu[1].cycle=1
ldst_fu[2].cycle=2

################################################### FU initialization End ###########################################




###################################################### CDB initialization ###########################################
cdb=namedlist('cdb','busy tag result')
cdb.busy=0
cdb.tag=-1
cdb.result=math.inf
#################################################### CDB initialization End #########################################



#################################################### Result Buffer initialization ###################################

def result_entry():
    result_entry=namedlist('result_entry','busy tag result address')
    temp=result_entry
    return temp

result_buffer=[]
for i in range (9):
    temp=result_entry()
    temp.busy=0
    temp.tag=-1
    temp.result=math.inf
    temp.address=-1
    result_buffer.extend([temp])

############################################ Result buffer initialization End #######################################


################################################### Memory initialization ###########################################
memory = read_memory("output/memory/memory@0.txt")
# for i in range(256):
#     memory.extend([0])
# memory[4] = 3
# memory[8] = 2
# memory[12] = 1
# memory[24] = 6
# memory[28] = 5
# memory[32] = 4
# memory[100] = 10
# memory[200] = 20
# memory[250] = 50
# memory[251] = 89
# memory[252] = 50

############################################## Memory initialization End ############################################

instructions_queue=read_instructions("iq.txt")
# print(instructions_queue)


while(1):
    cycle=cycle+1
    print("\n\n\nCycle=",cycle)

    '''Write'''
    write_result(int_add_rs,int_mul_rs,float_add_rs,float_mul_rs,shift_rs,comp_rs,nand_rs,ldst_buffer,xor_rs,int_register,fp_register,int_add_fu,int_mul_fu,float_add_fu,float_mul_fu,shift_fu,comp_fu,nand_fu,xor_fu,ldst_fu)

    '''Execute'''
    execute(instructions_queue,int_add_rs,int_mul_rs,float_add_rs,float_mul_rs,shift_rs,comp_rs,nand_rs,ldst_buffer,xor_rs,int_add_fu,int_mul_fu,float_add_fu,float_mul_fu,shift_fu,comp_fu,nand_fu,xor_fu,ldst_fu)
    print("###################### result_buffer #####################")
    for i in range(5):
        print(result_buffer[i].busy , result_buffer[i].tag ,  result_buffer[i].result, result_buffer[i].address)

    '''Issue'''
    print("pc =",pc)

    filename="output/pc/pc@"+str(cycle)+".txt"
    f=open(filename,"w")
    s=str(pc)+"\n"
    f.write(s)
    f.close()


    if(pc!=-1 and pc<len(instructions_queue)):
        # for j in int_register:
        #     print(j.busy , j.tag , j.data)

        issue(instructions_queue,int_add_rs,int_mul_rs,float_add_rs,float_mul_rs,shift_rs,comp_rs,nand_rs,xor_rs,ldst_buffer,int_register,fp_register)
    print("###################### int_register #####################")
    for i in range (5):
        print(int_register[i].busy , int_register[i].tag , int_register[i].data)

    print("###################### fp_register #####################")
    for i in range (5):
        print(fp_register[i].busy , fp_register[i].tag , fp_register[i].data)

    print("###################### int_add_rs #####################")
    for item in int_add_rs:
        print(item.busy , item.rs_tag , item.opcode , item.tag1 , item.value1 , item.tag2 , item.value2 , item.issued)

    print("###################### float_add_rs #####################")
    for item in float_add_rs:
        print(item.busy , item.rs_tag , item.opcode , item.tag1 , item.value1 , item.tag2 , item.value2 , item.issued)
    print("###################### ldst_buffer #####################")
    for i in ldst_buffer:
        print(i.busy , i.ldst_tag , i.opcode , i.address , i.tag , i.value , i.issued)


    filename="output/memory/memory@"+str(cycle)+".txt"
    f=open(filename,"w")
    for j in range(len(memory)):
        f.write(str(memory[j])+"\n")
    f.close()



    filename="output/int_register/int_register@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(16):
        s=str(int_register[i].busy)+" "+str(int_register[i].tag)+" "+str(int_register[i].data)+"\n"
        f.write(s)
    f.close()

    filename="output/fp_register/fp_register@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(16):
        s=str(fp_register[i].busy)+" "+str(fp_register[i].tag)+" "+str(fp_register[i].data)+"\n"
        f.write(s)
    f.close()

    # namedlist('rs_entry','rs_tag busy opcode tag1 value1 tag2 value2 issued')

    filename="output/int_add_rs/int_add_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(3):
        s=str(int_add_rs[i].rs_tag)+" "+str(int_add_rs[i].busy)+" "+str(int_add_rs[i].opcode)+" "+str(int_add_rs[i].tag1)+" "+str(int_add_rs[i].value1)+" "+str(int_add_rs[i].tag2)+" "+str(int_add_rs[i].value2)+" "+str(int_add_rs[i].issued)+"\n"
        f.write(s)
    f.close()

    filename="output/int_mul_rs/int_mul_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(3):
        s=str(int_mul_rs[i].rs_tag)+" "+str(int_mul_rs[i].busy)+" "+str(int_mul_rs[i].opcode)+" "+str(int_mul_rs[i].tag1)+" "+str(int_mul_rs[i].value1)+" "+str(int_mul_rs[i].tag2)+" "+str(int_mul_rs[i].value2)+" "+str(int_mul_rs[i].issued)+"\n"
        f.write(s)
    f.close()

    filename="output/float_add_rs/float_add_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(3):
        s=str(float_add_rs[i].rs_tag)+" "+str(float_add_rs[i].busy)+" "+str(float_add_rs[i].opcode)+" "+str(float_add_rs[i].tag1)+" "+str(float_add_rs[i].value1)+" "+str(float_add_rs[i].tag2)+" "+str(float_add_rs[i].value2)+" "+str(float_add_rs[i].issued)+"\n"
        f.write(s)
    f.close()

    filename="output/float_mul_rs/float_mul_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(3):
        s=str(float_mul_rs[i].rs_tag)+" "+str(float_mul_rs[i].busy)+" "+str(float_mul_rs[i].opcode)+" "+str(float_mul_rs[i].tag1)+" "+str(float_mul_rs[i].value1)+" "+str(float_mul_rs[i].tag2)+" "+str(float_mul_rs[i].value2)+" "+str(float_mul_rs[i].issued)+"\n"
        f.write(s)
    f.close()

    filename="output/shift_rs/shift_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(3):
        s=str(shift_rs[i].rs_tag)+" "+str(shift_rs[i].busy)+" "+str(shift_rs[i].opcode)+" "+str(shift_rs[i].tag1)+" "+str(shift_rs[i].value1)+" "+str(shift_rs[i].tag2)+" "+str(shift_rs[i].value2)+" "+str(shift_rs[i].issued)+"\n"
        f.write(s)
    f.close()

    filename="output/nand_rs/nand_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(2):
        s=str(nand_rs[i].rs_tag)+" "+str(nand_rs[i].busy)+" "+str(nand_rs[i].opcode)+" "+str(nand_rs[i].tag1)+" "+str(nand_rs[i].value1)+" "+str(nand_rs[i].tag2)+" "+str(nand_rs[i].value2)+" "+str(nand_rs[i].issued)+"\n"
        f.write(s)
    f.close()


    filename="output/xor_rs/xor_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(2):
        s=str(xor_rs[i].rs_tag)+" "+str(xor_rs[i].busy)+" "+str(xor_rs[i].opcode)+" "+str(xor_rs[i].tag1)+" "+str(xor_rs[i].value1)+" "+str(xor_rs[i].tag2)+" "+str(xor_rs[i].value2)+" "+str(xor_rs[i].issued)+"\n"
        f.write(s)
    f.close()

    filename="output/comp_rs/comp_rs@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(2):
        s=str(comp_rs[i].rs_tag)+" "+str(comp_rs[i].busy)+" "+str(comp_rs[i].opcode)+" "+str(comp_rs[i].tag1)+" "+str(comp_rs[i].value1)+" "+str(comp_rs[i].tag2)+" "+str(comp_rs[i].value2)+" "+str(comp_rs[i].issued)+"\n"
        f.write(s)
    f.close()

    #namedlist('ldst_entry','ldst_tag busy opcode address tag value issued')
    filename="output/ldst_buffer/ldst_buffer@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(4):
        s=str(ldst_buffer[i].ldst_tag)+" "+str(ldst_buffer[i].busy)+" "+str(ldst_buffer[i].opcode)+" "+str(ldst_buffer[i].address)+" "+str(ldst_buffer[i].tag)+" "+str(ldst_buffer[i].value)+" "+str(ldst_buffer[i].issued)+"\n"
        f.write(s)
    f.close()

    #namedlist('result_entry','busy tag result address')
    filename="output/result_buffer/result_buffer@"+str(cycle)+".txt"
    f=open(filename,"w")
    for i in range(9):
        s=str(result_buffer[i].busy)+" "+str(result_buffer[i].tag)+" "+str(result_buffer[i].result)+" "+str(result_buffer[i].address)+"\n"
        f.write(s)
    f.close()

    filename="output/cdb/cdb@"+str(cycle)+".txt"
    f=open(filename,"w")
    s=str(cdb.busy)+" "+str(cdb.tag)+" "+str(cdb.result)+"\n"
    f.write(s)
    f.close()



    cdb.busy=0
    cdb.tag=-1
    cdb.result=math.inf

    if(is_empty(int_add_rs) and is_empty(int_mul_rs) and is_empty(float_add_rs) and is_empty(float_mul_rs) and is_empty(shift_rs) and is_empty(nand_rs) and is_empty(xor_rs) and is_empty(comp_rs) and is_empty(ldst_buffer) ):
        filename="output/cycle.txt"
        f=open(filename,"w")
        s=str(cycle)+"\n"
        f.write(s)
        f.close()
        break


print(int(memory[200]))
