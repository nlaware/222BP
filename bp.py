from inspect import currentframe, getframeinfo

class BP:
  def __init__(self):
    self.pred = {}
    self.counter = 0
    self.branch = {}


  def check(self, expr):
    frameinfo = getframeinfo(currentframe().f_back)
    this_function = frameinfo.function
    this_line = frameinfo.lineno
    key = this_function + str(this_line)

    # now take action, using expr and key
    ''' Static *works kind of* '''
    # if key not in self.pred:
    #   self.pred[key] = [True]
    #
    # if self.pred[key][0] == expr:
    #   self.pred[key].append('correct')
    # else:
    #   self.pred[key].append('incorrect')

    ''' one bit *maybe working?* '''
    if key not in self.pred:
      self.pred[key] = [True, 'correct']

    if self.pred[key][-1] == 'correct':
      if self.pred[key][0] == expr:
        self.pred[key].append('correct')
      else:
        self.pred[key].append('incorrect')
    else:
      if self.pred[key][0] != expr:
        self.pred[key].append('correct')
      else:
        self.pred[key].append('incorrect')


    ''' Two bit '''
    if key not in self.pred:
      self.pred[key] = [True, 'correct']


    # here's a debug statement
    #print(key, 'this is expr:', expr)

  def print_summary(self):
    # print a summary
    total_correct = 0
    total_incorrect = 0
    for key in self.pred:
      correct = 0
      incorrect = 0
      for i in self.pred[key]:
        if i == 'correct':
          correct += 1
          total_correct += 1
        elif i == 'incorrect':
          incorrect += 1
          total_incorrect += 1
        else:
          pass
      # if incorrect != 0:
      total_percent = ((correct/(incorrect+correct))*100)
      print(key, ': #total =', correct + incorrect, '%correct =', format(total_percent, '.2f'))
      # else:
      #   total_percent = 0
      #   print(key, ': #total =', correct + incorrect, '%correct =', format(total_percent, '.2f'))

    print('Overall total =', total_correct + total_incorrect, '%correct = ',
          format((total_correct/(total_correct+total_incorrect)*100), '.2f'))
    print('#correct =', total_correct, '; #incorrect = ', total_incorrect)
    # print(self.pred)

#======================================================

bp_info = BP()
