from django.shortcuts import render
from django.views.generic import View
from .utils import is_json
from .mixin import HttpResponseMixin,SerializeMixin
import json
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import StudentForm


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(HttpResponseMixin,SerializeMixin,View):
	def get_object_by_id(self,id):
		try:
			s=Student.objects.get(id=id)
		except Student.DoesNotExist:
			s=None
		return s

	def get(self,request,*args,**kwargs):
		data = request.body
		valid_json = is_json(data)
		if not valid_json:
			return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status=400)
		pdata=json.loads(data)
		id=pdata.get('id',None)
		if id is not None:
			# student = Student.objects.get(id=id)
			std=self.get_object_by_id(id)
			if std is None:
				return self.render_to_http_response(json.dumps({'msg':'No matched Record Found with matched id'}),status=400)
			json_data=self.serialize([std,])
			return self.render_to_http_response(json_data)
		qs=Student.objects.all()
		json_data=self.serialize(qs)
		return self.render_to_http_response(json_data)
	
	def post(self,request,*args,**kwargs):
		data=request.body
		valid_json = is_json(data)
		if not valid_json:
			return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status=400)
		std_data=json.loads(data)
		form=StudentForm(std_data)
		if form.is_valid():
			form.save(commit=True)
			return self.render_to_http_response(json.dumps({'msg':'Resources created Successfully'}))
		if form.errors:
			json_data=json.dumps(form.errors)
			return self.render_to_http_response(json_data,status=400)

	def put(self,request,*args,**kwargs):
		data=request.body
		valid_json = is_json(data)
		if not valid_json:
			return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status=400)
		provided_data=json.loads(data)
		id=provided_data.get('id',None)
		if id is None:
			return self.render_to_http_response(json.dumps({'msg':'To perform updation, id is mandatory, plz provide'}),status=400)
		std=self.get_object_by_id(id)
		if std is None:
			return self.render_to_http_response(json.dumps({'msg':'No matched record Found with the given id!'}),status=400)
		original_data={
		'name':std.name,
		'marks':std.marks,
		'rollno':std.rollno,
		}
		original_data.update(provided_data)
		form=StudentForm(original_data,instance=std)
		if form.is_valid():
			form.save(commit=True)
			return self.render_to_http_response(json.dumps({'msg':'Resources updated Successfully'}))
		if form.errors:
			json_data=json.dumps(form.errors)
			return self.render_to_http_response(json_data,status=400)

	def delete(self,request,*args,**kwargs):
		data=request.body
		valid_json = is_json(data)
		if not valid_json:
			return self.render_to_http_response(json.dumps({'msg':'please provide valid json data only'}),status=400)
		provided_data=json.loads(data)
		id=provided_data.get('id',None)
		if id is None:
			return self.render_to_http_response(json.dumps({'msg':'To perform deletion, id is mandatory, plz provide'}),status=400)
		std=self.get_object_by_id(id)
		if std is None:
			return self.render_to_http_response(json.dumps({'msg':'No matched record Found with the given id!'}),status=400)
		status,deleted_item=std.delete()
		if status==1:
			json_data=json.dumps({'msg':'Resource deleted Successfully'})
			return self.render_to_http_response(json_data)
		json_data=json.dumps({'msg':'unable to delete ...plz try again'})
		return self. render_to_http_response(json_data,status=500)

















