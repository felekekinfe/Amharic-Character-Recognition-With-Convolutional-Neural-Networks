import cv2

def segment_letters(thresh):
    _,_,stats,_=cv2.connectedComponentsWithStats(thresh,connectivity=8)

    components=sorted([(stat[0],stat[1],stat[2],stat[3])for stat in stats[1:]],
                      key=lambda x: x[0])
    
    return [c for c in components if c[2]*c[3]>=50]
