from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets,status
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from vision_app.models import *
# nodes_model,realtimes_model,image_model,ultg_model,unit_model,model
from vision_app.serializer import nodes_serializer,realtimes_serializer,image_serializer
from datetime import datetime
from django.shortcuts import get_object_or_404

# Create your views here.


class Nodes_viewset(viewsets.ModelViewSet):
    queryset=nodes_model.objects.all()
    serializer_class=nodes_serializer
    lookup_field='node_id'
    # tes_unique=realtimes_model.objects.values('node').distinct()
    # print(tes_unique)

    @action(detail=True,methods=['post'])
    def upload_data(self,request,device_id=None):
        try:
            device=self.get_object()
            real_data=realtimes_model(
                node=device,
                Pressure=request.data.get('pressure'),
                Status_cam=request.data.get('status_cam'),
                Status_gauge=request.data.get('status_gauge'),
                )
            real_data.save()
            return Response(realtimes_serializer(real_data).data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def last_image(request, pk=None):
    if pk is None:
        return Response({'error': 'Node ID is required'}, status=400)

    images = image_model.objects.filter(node__node_id=pk).last()
    if not images:
        return Response({'error': 'No images found for this node'}, status=400)

    serializer = image_serializer(images, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def upload_image(request, id):
    """
    Upload an image for a specific node.
    
    Parameters:
    - id: node_id of the target node
    - request.FILES['photo']: The image file to upload
    
    Returns:
    - 201: Image uploaded successfully
    - 400: Invalid request or missing image
    - 404: Node not found
    """
    try:
        # Get the node instance
        node = get_object_or_404(nodes_model, node_id=id)
        
        # Check if image file is provided in the request
        if 'photo' not in request.FILES:
            return Response(
                {'error': 'No image file provided'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Create new image instance
        image = image_model.objects.create(
            node=node,
            photo=request.FILES['photo']
        )
        
        # Return success response
        return Response({
            'message': 'Image uploaded successfully',
            'image_id': image.id,
            'node_id': node.node_id,
            'photo_url': image.photo.url,
            'uploaded_at': image.uploaded_at
        }, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['POST'])
def tes(request):
    try:
        user=request.data.get('user')
        user_=user_model.objects.get(user_name=user)
        
        return Response({'data':user_.unit.values('ULTG').distinct()},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'err':str(e)},status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def Login_view(request):
    try:
        user=request.data.get('user')
        passd=request.data.get('pass')
        user=user_model.objects.filter(Q(user_name=user)&Q(password=passd)).first()
        if user:
            return Response({'response':f'welcome '},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'response':'not identified'},status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'err':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def upt_view(request):
    try:
        user=request.data.get('user')
        user_=user_model.objects.get(user_name=user)   
        return Response({'UPT':upt_model.objects.filter(upt_id__ultg_id__in=user_.unit.all()).values('UPT').distinct()}
                        ,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'err':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def ultg_view(request):
    try:
        user=request.data.get('user')
        user_=user_model.objects.get(user_name=user)   
        return Response({'ULTG':user_.unit.values('ULTG').distinct()},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'err':str(e)},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def gi_view(request):
    try:
        user=request.data.get('user')
        user_=user_model.objects.get(user_name=user)   
        return Response({'GIS':user_.unit.values('GIS').distinct()},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'err':str(e)},status=status.HTTP_400_BAD_REQUEST)

