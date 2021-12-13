#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#plot geometric mean for 
# fslmaths 4drest  -Tmean -mul -1 -add 4drest temp
# fslmaths 4drest  -bptf 77 8.68 temp
# fslmaths 4drest -s 2.548 temp
# fslmaths 3dt1  -kernel boxv 7 -dilM temp

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.DataFrame({'Method': ['distancemap','distancemap','distancemap','distancemap','niimath','niimath','niimath','niimath'],
					'Voxels': [12792000, 6427200, 6396000, 2142400, 12792000, 6427200, 6396000, 2142400],
					'Time (s)': [4281.96, 1101.61, 1054.13, 95.63, 1.33, 0.74, 0.6, 0.22]})
sns.set()
ax = sns.lineplot(x='Voxels', y='Time (s)', hue='Method', data=df, marker='o')
plt.savefig('distancemap.png', dpi=300)