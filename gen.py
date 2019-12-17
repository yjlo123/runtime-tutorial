# create venv
# python3 -m venv env

import markdown
from datetime import datetime

md = markdown.Markdown(extensions=['markdown.extensions.fenced_code'])

file_data = None
with open('raw.md') as f:
	file_data = f.read()
	#print(file_data)

data = md.convert(file_data)

header_list = []

# link
i = len(data)
target = '<a '
while i != -1:
	i = data.rfind(target, 0, i)
	if i == -1:
		break
	#print(i)
	j = i + len(target)
	data = data[:j] + 'target="_blank" ' + data[j:]
	data = '{}target="_blank" {}'.format(data[:j], data[j:])

# header
i = len(data)
target = '<h2>'
while i != -1:
	i = data.rfind(target, 0, i)
	if i == -1:
		break
	j = i + len(target)
	k = data[i:].find('</h2>')
	#print(j, i+k)
	head_text = data[j:i+k]
	header_id = head_text.lower().replace(' ', '-')
	header_list.insert(0, (head_text, header_id))
	data = '{} id="{}"{}'.format(data[:j-1], header_id, data[j-1:])

# code block
i = len(data)
target = 'class="code-block"'
prefix = '><code '
while i != -1:
	i = data.rfind(target, 0, i)
	if i == -1:
		break
	#print(i)
	j = i + len(target)
	data = '{} {}{}{}'.format(data[:i-len(prefix)], target, prefix[:-1], data[j:])

# runtime embedded box
i = len(data)
target = 'runtime-embedded-box'
prefix = '<pre><code class="'
postfix = '</code></pre>'
box_extra_class = {
	0: '',
	1: 'runtime-show-canvas',
	2: 'runtime-hide-console',
	3: 'runtime-show-canvas runtime-hide-console',
}
while i != -1:
	i = data.rfind(target, 0, i) # class start
	if i == -1:
		break
	#print(i)
	j = i + len(target) # class params start
	k = j + data[j:].find('"') # class end
	l = k + data[k:].find(postfix) # code block end
	box_style = data[j+1:k].split('-') # [type, height]
	data = '{}<div class="runtime-embedded-box {}" style="width: 100%; height: {}px;">{}</div>{}'.format(
		data[:i-len(prefix)], 
		box_extra_class[int(box_style[0])],
		box_style[1], 
		data[k+2:l], 
		data[l+len(postfix):]
		)


template = ''
with open('template.html') as f:
	template = f.read()

toc = '\n'.join(['<li><a href="#{}">{}</a></li>'.format(header[1], header[0]) for header in header_list])

out_data = template.replace('{{toc}}', toc)
now = datetime.now()
out_data = out_data.replace('{{date}}', now.strftime("%d %b, %Y"))
out_data = out_data.replace('{{contents}}', data)

with open('out.html', 'w') as f:
	f.write(out_data)
