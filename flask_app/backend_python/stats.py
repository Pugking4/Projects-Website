import os
import json
import collections

class overview_stats:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def test(self):
        print(200)

    def get_stats_data(self):
        data = []
        files = os.listdir(self.file_path)
        #print(files)
        for file in files:
            if file.endswith('.json'):
                #print(file)
                with open(self.file_path + '\\' + file, 'r') as f:
                    data.append(json.load(f))
        self.data = data
    
    def calculate_stats(self):
        #print(len(self.data))
        c = collections.defaultdict(int)

        #init avg variables
        internal_level_data = []
        internal_level_data_none = []
        all_note_type_ratio_data = []
        taps_ratio_data = []
        holds_ratio_data = []
        slides_ratio_data = []
        touch_ratio_data = []
        breaks_ratio_data = []

        #custom variables
        #count each level and internal level p2 picks
        p2_picks = {}
        p2_picks_count = c
        parent_p2_picks = []
        p2_level_picks = {}
        p2_picks_none = {}

        chart_count = 0
        for day in self.data:
            #print(len(day))
            for chart in day:

                #init chart attributes
                title = chart['title']
                difficulty = chart['difficulty']
                score = chart['score']
                deluxe_score = chart['deluxe_score']
                type = chart['type']
                time = chart['time']
                track = chart['track']
                img_link = chart['img_link']
                combo = chart['combo']
                sync = chart['sync']
                place = chart['place']
                players = chart['players']
                new_record = chart['new_record']
                new_record_deluxe = chart['new_record_deluxe']
                taps = chart['taps']
                cp_taps = chart['taps']['critical_perfect']
                p_taps = chart['taps']['perfect']
                gr_taps = chart['taps']['great']
                go_taps = chart['taps']['good']
                m_taps = chart['taps']['miss']
                holds = chart['holds']
                cp_holds = chart['holds']['critical_perfect']
                p_holds = chart['holds']['perfect']
                gr_holds = chart['holds']['great']
                go_holds = chart['holds']['good']
                m_holds = chart['holds']['miss']
                slides = chart['slides']
                cp_slides = chart['slides']['critical_perfect']
                p_slides = chart['slides']['perfect']
                gr_slides = chart['slides']['great']
                go_slides = chart['slides']['good']
                m_slides = chart['slides']['miss']
                touch = chart['touch']
                cp_touch = chart['touch']['critical_perfect']
                p_touch = chart['touch']['perfect']
                gr_touch = chart['touch']['great']
                go_touch = chart['touch']['good']
                m_touch = chart['touch']['miss']
                breaks = chart['breaks']
                cp_breaks = chart['breaks']['critical_perfect']
                p_breaks = chart['breaks']['perfect']
                gr_breaks = chart['breaks']['great']
                go_breaks = chart['breaks']['good']
                m_breaks = chart['breaks']['miss']
                player2 = chart['player2']
                max_combo = chart['max_combo']
                max_sync = chart['max_sync']
                rating_gain = chart['rating_gain']
                current_rating = chart['current_rating']
                fast = chart['fast']
                late = chart['late']
                internal_level = chart['internal_level']
                level = chart['level']


                #Get note stats
                total_taps = sum(taps.values())
                total_holds = sum(holds.values())
                total_slides = sum(slides.values())
                total_touch = sum(touch.values())
                total_breaks = sum(breaks.values())

                #Avg stat prep
                #Avg internal level
                if internal_level != None:
                    internal_level_data.append(float(internal_level))
                    internal_level_data_none.append(float(internal_level))
                else:
                    try:
                        temp_level = float(level)
                    except:
                        temp_level = float(level.replace('+', '')) + 0.7
                    internal_level_data_none.append(temp_level)
                
                #Avg all note type ratio
                total_notes = total_taps + total_holds + total_slides + total_touch + total_breaks
                total_cp = cp_taps + cp_holds + cp_slides + cp_touch + cp_breaks
                total_p = p_taps + p_holds + p_slides + p_touch + p_breaks
                total_gr = gr_taps + gr_holds + gr_slides + gr_touch + gr_breaks
                total_go = go_taps + go_holds + go_slides + go_touch + go_breaks
                total_m = m_taps + m_holds + m_slides + m_touch + m_breaks

                cp_ratio = total_cp / total_notes
                p_ratio = total_p / total_notes
                gr_ratio = total_gr / total_notes
                go_ratio = total_go / total_notes
                m_ratio = total_m / total_notes

                all_note_type_ratio_data.append([cp_ratio, p_ratio, gr_ratio, go_ratio, m_ratio])

                #Avg taps ratio
                cp_taps_ratio = cp_taps / total_taps
                p_taps_ratio = p_taps / total_taps
                gr_taps_ratio = gr_taps / total_taps
                go_taps_ratio = go_taps / total_taps
                m_taps_ratio = m_taps / total_taps

                taps_ratio_data.append([cp_taps_ratio, p_taps_ratio, gr_taps_ratio, go_taps_ratio, m_taps_ratio])

                #Avg holds ratio
                cp_holds_ratio = cp_holds / total_holds
                p_holds_ratio = p_holds / total_holds
                gr_holds_ratio = gr_holds / total_holds
                go_holds_ratio = go_holds / total_holds
                m_holds_ratio = m_holds / total_holds

                holds_ratio_data.append([cp_holds_ratio, p_holds_ratio, gr_holds_ratio, go_holds_ratio, m_holds_ratio])

                #Avg slides ratio
                cp_slides_ratio = cp_slides / total_slides
                p_slides_ratio = p_slides / total_slides
                gr_slides_ratio = gr_slides / total_slides
                go_slides_ratio = go_slides / total_slides
                m_slides_ratio = m_slides / total_slides

                slides_ratio_data.append([cp_slides_ratio, p_slides_ratio, gr_slides_ratio, go_slides_ratio, m_slides_ratio])

                #Avg touch ratio
                if total_touch > 0:
                    cp_touch_ratio = cp_touch / total_touch
                    p_touch_ratio = p_touch / total_touch
                    gr_touch_ratio = gr_touch / total_touch
                    go_touch_ratio = go_touch / total_touch
                    m_touch_ratio = m_touch / total_touch

                    touch_ratio_data.append([cp_touch_ratio, p_touch_ratio, gr_touch_ratio, go_touch_ratio, m_touch_ratio])

                #Avg breaks ratio
                cp_breaks_ratio = cp_breaks / total_breaks
                p_breaks_ratio = p_breaks / total_breaks
                gr_breaks_ratio = gr_breaks / total_breaks
                go_breaks_ratio = go_breaks / total_breaks
                m_breaks_ratio = m_breaks / total_breaks

                breaks_ratio_data.append([cp_breaks_ratio, p_breaks_ratio, gr_breaks_ratio, go_breaks_ratio, m_breaks_ratio])
                
                #p2 level and internal level picks count
                if 'internal_level' not in p2_picks and 'level' not in p2_picks:
                    p2_picks['internal_level'] = {}
                    p2_picks['level'] = {}

                if player2 not in p2_picks['internal_level'] and player2 not in p2_picks['level']:
                    p2_picks['internal_level'][player2] = {}
                    p2_picks['level'][player2] = {}

                if player2 != None:
                    if level not in p2_picks['level'][player2]:
                        p2_picks['level'][player2][level] = 1
                    else:
                        p2_picks['level'][player2][level] += 1

                    if internal_level not in p2_picks['internal_level'][player2]:
                        p2_picks['internal_level'][player2][internal_level] = 1
                    else:
                        p2_picks['internal_level'][player2][internal_level] += 1



                #Average constant level of charts I play with other people with 2. applied
                if player2 not in p2_picks_none:
                    p2_picks_none[player2] = {}

                if player2 != None:
                    if internal_level not in p2_picks_none[player2]:
                        if internal_level:
                            p2_picks_none[player2][internal_level] = 1
                        else:
                            try:
                                temp_level = float(level)
                            except:
                                temp_level = float(level.replace('+', '')) + 0.7
                            p2_picks_none[player2][temp_level] = 1
                    else:
                        if internal_level:
                            p2_picks_none[player2][internal_level] += 1
                        else:
                            try:
                                temp_level = float(level)
                            except:
                                temp_level = float(level.replace('+', '') + 0.7)
                            p2_picks_none[player2][temp_level] += 1

                



                
                


        #Avg stat calculations
        #internal level
        avg_internal_level = sum(internal_level_data) / len(internal_level_data)
        avg_internal_level_none = sum(internal_level_data_none) / len(internal_level_data_none)

        #this code 💀
        #all note type ratio
        avg_cp_ratio = sum([x[0] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_p_ratio = sum([x[1] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_gr_ratio = sum([x[2] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_go_ratio = sum([x[3] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)
        avg_m_ratio = sum([x[4] for x in all_note_type_ratio_data]) / len(all_note_type_ratio_data)

        avg_notes_ratio_dict = {'avg_cp_ratio': avg_cp_ratio, 'avg_p_ratio': avg_p_ratio, 'avg_gr_ratio': avg_gr_ratio, 'avg_go_ratio': avg_go_ratio, 'avg_m_ratio': avg_m_ratio}

        #taps ratio
        avg_cp_taps_ratio = sum([x[0] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_p_taps_ratio = sum([x[1] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_gr_taps_ratio = sum([x[2] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_go_taps_ratio = sum([x[3] for x in taps_ratio_data]) / len(taps_ratio_data)
        avg_m_taps_ratio = sum([x[4] for x in taps_ratio_data]) / len(taps_ratio_data)

        avg_taps_ratio_dict = {'avg_cp_taps_ratio': avg_cp_taps_ratio, 'avg_p_taps_ratio': avg_p_taps_ratio, 'avg_gr_taps_ratio': avg_gr_taps_ratio, 'avg_go_taps_ratio': avg_go_taps_ratio, 'avg_m_taps_ratio': avg_m_taps_ratio}

        #holds ratio
        avg_cp_holds_ratio = sum([x[0] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_p_holds_ratio = sum([x[1] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_gr_holds_ratio = sum([x[2] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_go_holds_ratio = sum([x[3] for x in holds_ratio_data]) / len(holds_ratio_data)
        avg_m_holds_ratio = sum([x[4] for x in holds_ratio_data]) / len(holds_ratio_data)

        avg_holds_ratio_dict = {'avg_cp_holds_ratio': avg_cp_holds_ratio, 'avg_p_holds_ratio': avg_p_holds_ratio, 'avg_gr_holds_ratio': avg_gr_holds_ratio, 'avg_go_holds_ratio': avg_go_holds_ratio, 'avg_m_holds_ratio': avg_m_holds_ratio}

        #slides ratio
        avg_cp_slides_ratio = sum([x[0] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_p_slides_ratio = sum([x[1] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_gr_slides_ratio = sum([x[2] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_go_slides_ratio = sum([x[3] for x in slides_ratio_data]) / len(slides_ratio_data)
        avg_m_slides_ratio = sum([x[4] for x in slides_ratio_data]) / len(slides_ratio_data)

        avg_slides_ratio_dict = {'avg_cp_slides_ratio': avg_cp_slides_ratio, 'avg_p_slides_ratio': avg_p_slides_ratio, 'avg_gr_slides_ratio': avg_gr_slides_ratio, 'avg_go_slides_ratio': avg_go_slides_ratio, 'avg_m_slides_ratio': avg_m_slides_ratio}

        #touch ratio
        avg_cp_touch_ratio = sum([x[0] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_p_touch_ratio = sum([x[1] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_gr_touch_ratio = sum([x[2] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_go_touch_ratio = sum([x[3] for x in touch_ratio_data]) / len(touch_ratio_data)
        avg_m_touch_ratio = sum([x[4] for x in touch_ratio_data]) / len(touch_ratio_data)

        avg_touch_ratio_dict = {'avg_cp_touch_ratio': avg_cp_touch_ratio, 'avg_p_touch_ratio': avg_p_touch_ratio, 'avg_gr_touch_ratio': avg_gr_touch_ratio, 'avg_go_touch_ratio': avg_go_touch_ratio, 'avg_m_touch_ratio': avg_m_touch_ratio}

        #breaks ratio
        avg_cp_breaks_ratio = sum([x[0] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_p_breaks_ratio = sum([x[1] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_gr_breaks_ratio = sum([x[2] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_go_breaks_ratio = sum([x[3] for x in breaks_ratio_data]) / len(breaks_ratio_data)
        avg_m_breaks_ratio = sum([x[4] for x in breaks_ratio_data]) / len(breaks_ratio_data)

        avg_breaks_ratio_dict = {'avg_cp_breaks_ratio': avg_cp_breaks_ratio, 'avg_p_breaks_ratio': avg_p_breaks_ratio, 'avg_gr_breaks_ratio': avg_gr_breaks_ratio, 'avg_go_breaks_ratio': avg_go_breaks_ratio, 'avg_m_breaks_ratio': avg_m_breaks_ratio}

        #Who I play with the most
        total_charts_played_p2 = {}
        #most_played_p2 = max(p2_picks['level'], key=p2_picks['level'].get)
        for player in p2_picks['level']:
            temp_sum = 0
            for level in p2_picks['level'][player]:
                temp_sum += p2_picks['level'][player][level]
            if player != None:
                total_charts_played_p2[player] = temp_sum
        
        #Average constant level of charts I play with other people
        #remove rounding at end
        avg_internal_level_p2 = {}
        for player in p2_picks['internal_level']:
            temp_sum = 0
            temp_count = 0
            for internal_level in p2_picks['internal_level'][player]:
                if internal_level == None:
                    continue
                temp_count += int(p2_picks['internal_level'][player][internal_level])
                temp_sum += int(p2_picks['internal_level'][player][internal_level]) * float(internal_level)
            if player != None:
                avg_internal_level_p2[player] = round(temp_sum / temp_count, 1)


        #Average constant level of charts I play with other people with 2. applied
        avg_internal_level_p2_none = {}
        for player in p2_picks_none:
            temp_sum = 0
            temp_count = 0
            for internal_level in p2_picks_none[player]:
                temp_count += int(p2_picks_none[player][internal_level])
                temp_sum += int(p2_picks_none[player][internal_level]) * float(internal_level)
            if player != None:
                avg_internal_level_p2_none[player] = round(temp_sum / temp_count, 1)
        

            
        #print('avg_notes_ratio_dict:', avg_notes_ratio_dict)
        #print('avg_taps_ratio_dict:', avg_taps_ratio_dict)
        #print('avg_holds_ratio_dict:', avg_holds_ratio_dict)
        #print('avg_slides_ratio_dict:', avg_slides_ratio_dict)
        #print('avg_touch_ratio_dict:', avg_touch_ratio_dict)
        #print('avg_breaks_ratio_dict:', avg_breaks_ratio_dict)

        #print('internal_level p2_picks:', p2_picks['internal_level'])
        #print('level p2_picks_none:', p2_picks['level'])

        #print('avg_internal_level', avg_internal_level)
        #print('avg_internal_level_none', avg_internal_level_none)


        #print(max(total_charts_played_p2, key=total_charts_played_p2.get), max(total_charts_played_p2.values()))

        print(avg_internal_level_p2)
        print(avg_internal_level_p2_none)



        

instance = overview_stats(r'C:\Users\joshu\Documents\GitHub\Projects-Website\flask_app\records')

instance.get_stats_data()

instance.calculate_stats()