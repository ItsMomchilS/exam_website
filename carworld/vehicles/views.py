from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, FormView, ListView, UpdateView, DeleteView

from carworld.common.forms import CommentForm
from carworld.common.models import Comment
from carworld.core.views import PostOnlyView, BootStrapFormViewMixin
from carworld.vehicles.forms import EditVehicleForm
from carworld.vehicles.models import Vehicle, Like


class ListVehiclesView(ListView):
    template_name = 'vehicles/vehicle_list.html'
    context_object_name = 'vehicles'
    model = Vehicle


class VehicleDetailsView(DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle_detail.html'
    context_object_name = 'vehicle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = context['vehicle']

        vehicle.likes_count = vehicle.like_set.count()
        is_owner = vehicle.user == self.request.user

        is_liked_by_user = vehicle.like_set.filter(user_id=self.request.user.id) \
            .exists()
        context['comment_form'] = CommentForm(
            initial={
                'pet_pk': self.object.id,
            }
        )
        context['comments'] = vehicle.comment_set.all()
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user

        return context


class CommentVehicleView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            vehicle=vehicle,
            user=self.request.user,
        )
        comment.save()

        return redirect('vehicle details', vehicle.id)

    def form_invalid(self, form):
        pass


class LikeVehicleView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = vehicle.like_set.filter(user_id=self.request.user.id) \
            .first()
        if like_object_by_user:
            like_object_by_user.delete()
        else:
            like = Like(
                vehicle=vehicle,
                user=self.request.user,
            )
            like.save()
        return redirect('vehicle details', vehicle.id)


class CreateVehicleView(LoginRequiredMixin, BootStrapFormViewMixin, CreateView):
    model = Vehicle
    fields = ('ad_type', 'vehicle_model', 'description', 'image', 'create_year', 'type', 'price')
    success_url = reverse_lazy('list vehicles')
    template_name = 'vehicles/vehicle_create.html'

    def form_valid(self, form):
        vehicle = form.save(commit=False)
        vehicle.user = self.request.user
        vehicle.save()
        return super().form_valid(form)


class EditVehicleView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    template_name = 'vehicles/vehicle_edit.html'
    form_class = EditVehicleForm
    success_url = reverse_lazy('list vehicles')


class DeleteVehicleView(LoginRequiredMixin, DeleteView):
    template_name = 'vehicles/vehicle_delete.html'
    model = Vehicle
    success_url = reverse_lazy('list vehicles')
