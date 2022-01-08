import time
import pdb

def section(data, head , tail, drawdata,timetick):
    border = head
    pivot = data[tail]

    drawdata(data, colors(len(data), head, tail, border, border))
    time.sleep(timetick)

    for j in range(head, tail):
        if (data[j] < pivot):
            drawdata(data, colors(len(data), head, tail, border, j, True))
            data[border], data[j] = data[j], data[border]
            border += 1
        drawdata(data, colors(len(data), head, tail, border, j))
        time.sleep(timetick)
    # swapping pivot element with border value
    drawdata(data, colors(len(data), head, tail, border, tail, True))
    time.sleep(timetick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawdata, timetick):
    start = time.time()
    # pdb.set_trace()
    if head < tail:
        sectionIdx = section(data, head , tail, drawdata,timetick)

        # Left section
        quick_sort(data, head, sectionIdx-1, drawdata, timetick)
        # right section
        quick_sort(data, sectionIdx+1, tail, drawdata, timetick)
    elapsed_time_fl = (time.time() - start)
    return round(elapsed_time_fl, 2)

def colors(data_length, head, tail, border, current_idx, is_swapping = False ):
    colors_list = []
    for i in range(data_length):
        if i>= head and i<=tail:
            colors_list.append('#696969')
        else:
            colors_list.append('#FFFFF0')
        if i==tail:
            colors_list[i] = "orange"
        elif i==border:
            colors_list[i]="#B22222"
        elif i==current_idx:
            colors_list[i]='#FFD700'
        if is_swapping:
            if i == border or i == current_idx:
                colors_list[i]="#228B22"
    return colors_list