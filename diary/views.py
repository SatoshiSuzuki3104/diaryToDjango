# from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day


# def index(request):
#     # return render(request, 'diary/day_list.html')
#     context = {
#         'day_list': Day.objects.all(),
#     }
#     return render(request, 'diary/day_list.html', context)

class IndexView(generic.ListView):
    model = Day
    paginate_by = 3


# def add(request):
#     # context = {
#     #     'form': DayCreateForm(),
#     # }
#     #
#     # return render(request, 'diary/day_form.html', contextsi)
#
#     # 送信内容をもとにフォームを作る、POSTじゃなければ、からのフォーム
#     form = DayCreateForm(request.POST or None)
#
#     # method=POST、つまり送信ボタン押下時、入力内容が問題なければ
#     if request.method == 'POST' and form.is_valid():
#         form.save()  # SQL文ではinsert関数が実行される
#         return redirect('diary:index') # 二重投稿を防ぐため
#
#     # 通常じのページアクセスや、入力内容に誤りがあればまたページを表示
#     context = {
#         'form': form
#     }
#
#     return render(request, 'diary/day_form.html', context)


class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm
    # fields = '__all__'
    success_url = reverse_lazy('diary:index')


# def update(request, pk):
#     # urlのpkをもとに、Dayを取得
#     day = get_object_or_404(Day, pk=pk)
#
#     # フォームに、取得したDayを紐ずける
#     form = DayCreateForm(request.POST or None, instance=day)
#
#     # method=POST、つまり送信ボタン押下じに、入力内容が問題なければ
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect("diary:index")
#
#     # 通常じのページアクセスや、入力内容に誤りがなければまたページを表I
#     context = {
#         'form': form
#     }
#     return render(request, 'diary/day_form.html', context)


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


# def delete(request, pk):
#     # urlのpkをもとに、Dayを取得
#     day = get_object_or_404(Day, pk=pk)
#
#     # method=POST、つまり送信ボタン押下じに、入力内容が問題なければ
#     if request.method == 'POST':
#         day.delete()
#         return redirect("diary:index")
#
#     # 通常じのページアクセスや、入力内容に誤りがなければまたページを表I
#     context = {
#         'day': day
#     }
#     return render(request, 'diary/day_confirm_delete.html', context)


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy("diary:index")

# def detail(request, pk):
#     # urlのpkをもとに、Dayを取得
#     day = get_object_or_404(Day, pk=pk)
#
#     # 通常じのページアクセスや、入力内容に誤りがなければまたページを表I
#     context = {
#         'day': day
#     }
#     return render(request, 'diary/day_detail.html', context)


class DetailView(generic.DetailView):
    model = Day