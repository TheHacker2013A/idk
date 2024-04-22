from tkinter import*
window = Tk()

def submit():
    input1 = entry.get()
    wordsplitted = list(map(str,input1.split()))
    bannedwords = [   'bad',
    'dog',
    'donkey',
    'damn',
    'hell',
    'shit',
    'asshole',
    'bitch',
    'fuck',
    'cunt',
    'bastard',
    'dick',
    'pussy',
    'cock',
    'whore',
    'slut',
    'faggot',
    'nigger',
    'chink',
    'spic',
    'kike',
    'retard',
    'moron',
    'idiot',
    'stupid',
    'douchebag',
    'asshat',
    'motherfucker',
    'son of a bitch',
    'twat',
    'arsehole',
    'wanker',
    'bollocks',
    'prick',
    'knob',
    'jackass',
    'twatwaffle',
    'cum',
    'cocksucker',
    'motherfucking',
    'piss',
    'whore',
    'slag',
    'bimbo',
    'slutty',
    'douchecanoe',
    'fucker',
    'assclown',
    'douche',
    'wankstain',
    'scumbag',
    'molest',
    'rape',
    'pedophile',
    'incest',
    'bestiality',
    'genocide',
    'terrorist',
    'hate',
    'bigot',
    'racist',
    'sexist',
    'homophobic',
    'transphobic',
    'xenophobic',
    'ableist',
    'islamophobic',
    'antisemitic',
    'سيء',
    'كلب',
    'حمار',
    'لعنة',
    'جحيم',
    'قرف',
    'كلبة',
    'نكاح',
    'كس',
    'زب',
    'عاهرة',
    'فاسقة',
    'مثلي الجنس',
    'نيغر',
    'صيني',
    'مقزز',
    'حمار',
    'تجاهل',
    'أغبى',
    'غبي',
    'لئيم',
    'جلبة',
    'سوء الحظ',
    'تافه',
    'سخيف',
    'غطاء',
    'بابي',
    'نوع أمي',
    'خول',
    'حمار',
    'خراء',
    'لصق',
    'شرموطة',
    'لتنظيم',
    'لعين',
    'بغيض',
    'قذر',
    'عنصري',
    'جنسي',
    'تعصبي',
    'كراهية',
    'قومي',
    'فاشي',
    'تمييزي',
    'معادٍ',
    ]


    for i in wordsplitted:
      if i in bannedwords:
          global badworddectected
          print("word deleted")
          entry.delete(0,END)
          badworddectected = Label(window,text="bad word")
          badworddectected.pack()
    else:
         print(i)
def delete():
    global badworddectected
    badworddectected.destroy()
    entry.delete(0,END)
submit = Button(window,text="submit",command=submit)
delete = Button(window,text="delete",command=delete)
entry =Entry()
word = "none"
entry.pack()
submit.pack()
delete.pack()
print(entry)


window.mainloop()