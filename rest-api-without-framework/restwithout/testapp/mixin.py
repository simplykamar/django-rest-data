from django.http import HttpResponse

class HttpResponseMixin(object):
	def render_to_http_response(self,data,status=200):
		return HttpResponse(data,content_type='application/json',status=status)

from django.core.serializers import serialize
import json

class SerializeMixin(object):
	def serialize(self,qs):
		json_data=serialize('json',qs)
		pdict=json.loads(json_data)
		final_data=[]
		for obj in pdict:
			final_data.append(obj['fields'])
		json_data=json.dumps(final_data)
		return json_data