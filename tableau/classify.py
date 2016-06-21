def classify(rgb_tuple):
    # rgb값은 튜플로 받을 수 있도록 입력 전에 튜플로 만들어주는 코딩을 짤 것
    # 색채심리 DB("Final Color Code.xlsx")를 아래 colors에 dict으로 저장
    # 예제로 몇개만 입력
    colors = {"Red": (255,0,0),
              "Green": (0,255,0),
              "Blue": (0, 0, 255),
              "Black": (0,0,0),
              "White": (255,255,255),
              "Neutral Gray": (137,141,141)
              }

    euclidean = lambda x,y: (x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2
    distances = {k: euclidean(v, rgb_tuple) for k, v in colors.items()}
    color = min(distances, key=distances.get)
    return color

exrgb = (194,202,186)
result1 = classify(exrgb)
print(result1)