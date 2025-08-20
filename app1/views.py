from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *
from fpdf import FPDF
    

def Menu(request):
    if request.method == 'GET':
        search_word = request.GET.get('word', '')
        if search_word:
            cars = Cars.objects.filter(title__icontains=search_word)
        else:
            cars = Cars.objects.all()

        context={
            'title': 'Menu',
            'cars': cars,
            'carmodels': CarModel.objects.all(),
            'search_word': search_word,
        }

    else:
        context = {
            'title': 'Menu',
            'cars': Cars.objects.all(),
            'carmodels': CarModel.objects.all(),
            'form': SearchForm(),
        }


    return render(request, 'index.html', context=context)



class CreateCar(CreateView):
    model=Cars
    form_class=CarsForm
    template_name='create_car.html'
    success_url=reverse_lazy('home')


class CreateCarModel(CreateView):
    model=CarModel
    form_class=CarModelForm
    template_name='create_carmodel.html'
    success_url=reverse_lazy('home')


class UpdateCar(UpdateView):
    model=Cars
    form_class=CarsForm
    template_name='update_car.html'
    success_url=reverse_lazy('home')
    pk_url_kwarg = 'pk'





class DetailCar(DetailView):
    model=Cars
    template_name='detail_car.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'detail_car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail Car'
        context['car'] = Cars.objects.get(pk=self.kwargs['pk'])

        return context
    
def PdfDownload(request, pk):
    car= Cars.objects.get(pk=pk)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Sarlavha
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Avtomobil Malumotlari", ln=True, align="C")
    pdf.ln(10)

    # Avtomobil ma'lumotlari
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Model: {car.carmodel.title}", ln=True)
    pdf.cell(0, 10, f"Nom: {car.title}", ln=True)
    pdf.cell(0, 10, f"Kontext: {car.context}", ln=True)
    pdf.cell(0, 10, f"Yaratilgan: {car.create_ed}", ln=True)
    pdf.cell(0, 10, f"O'zgartirilgan: {car.update_ed}", ln=True)
    pdf.cell(0, 10, f"Foto: {car.photo.url if car.photo else 'Yo\'q'}", ln=True)
    pdf.cell(0, 10, f"Holat: {'Aktiv' if car.is_bool else 'Noaktiv'}", ln=True)
    pdf.cell(0, 10, f"Ko'rishlar: {car.views}", ln=True)
    

    pdf_output = pdf.output(dest='S').encode('latin1')

    
    response = HttpResponse(pdf_output, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="car_{pk}.pdf"'
    return response

def DeleteCar(request, pk):
    car = Cars.objects.get(pk=pk)
    car.delete()
    return HttpResponseRedirect(reverse_lazy('home'))