#트리의 순환, 분할정복,tree, sol220629
import sys
sys.setrecursionlimit(10**4)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

tmp=[]
def find(ins,ine,posts,poste):
    if ins==ine:
        tmp.append(inorder[ins])
        return
    elif ins>ine or posts>poste:
        return
    
    root = postorder[poste]
    tmp.append(root)
    #inorder 배열에서 root의 idx
    in_root_idx = inorder.index(root)
    l_num = in_root_idx-ins
    r_num = ine-in_root_idx
    
    #왼쪽은 같아.
    find(ins, in_root_idx-1, posts, posts+l_num-1)
    #오른쪽은
    find(in_root_idx+1,ine , posts+l_num , poste-1)
    return

find(0,N-1,0,N-1)
print(*tmp)
