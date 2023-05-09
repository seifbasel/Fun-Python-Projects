# def dda_Line_con(x1, y1, x2, y2) :
#     delta_x = x2 - x1 #delta x
#     delta_y = y2 - y1 #delta y
#     len = max(delta_x, delta_y) #max
#     delta_x = delta_x / len 
#     delta_y = delta_y / len
#     x = float(x1) # x first point
#     y = float(y1) # y first point
#     print(round(x) , " , ", round(y))
#     for _ in range(len) :
#         x += delta_x
#         y += delta_y
#         print(round(x) , " , ", round(y))


# dda_Line_con(0,0,5,6)





# def breesnham_line_Con(x1, y1, x2, y2) :
#     dx = x2 - x1 #delta x
#     dy = y2 - y1 #delta y
#     p = 2 * dy - dx #first point p
#     x = x1 # x first point
#     y = y1 # y first point
#     print(x, " , ", y)
#     while x < x2 :
#         x += 1
#         if p < 0 :
#             p += 2 * dy
#         else :
#             y += 1
#             p += 2 * dy - 2 * dx
#             print(x, " , ", y)

# breesnham_line_Con(0,0,5,6) 



# def mid_Point_line_con(x1, y1, x2, y2) :

#     dy = y2 - y1 #delta x
#     dx = x2 - x1 #delta y
        
#     d = (2 * dy) - dx # first value of d
#     x = x1
#     y = y1
#     print(x, ",", y)
#     while (x < x2) :
#         x += 1
#         if(d < 0) :
#             d = d + (2*dy)
#         else :
#             d = d + 2*(dy - dx)
#             y += 1
#         print(x, ",", y)

        
# mid_Point_line_con(0, 0, 5, 6)




# def mid_point_circle_con(x1, y1, r) :
#     x , y = 0, r #start point ,  radius
#     p = 1 - r
#     print(x1 + x, y1 + y) #first point

#     while y >= x :
#         x += 1
#         if p > 0 :
#             y -= 1
#             p = p + 2 * (x - y) + 1
#         else :
#             p = p + 2 * x + 1
#         print(x1 + x, y1 + y)
# mid_point_circle_con(0, 0, 5)





# def breesnham_circle_con(x1, y1, r) :
#     x , y = 0, r  #start point ,  radius
#     d = 3 - 2 * r  
#     print(x1 + x, y1 + y) #first point

#     while y >= x :
#         x += 1
#         if d > 0 :
#             y -= 1
#             d = d + 4 * (x - y) + 10
#         else :
#             d = d + 4 * x + 6
#             print(x1 + x, y1 + y)
# breesnham_circle_con(0, 0, 4)