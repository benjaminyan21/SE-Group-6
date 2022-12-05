#Railtrak is our web app and this site is designed to change the method of transportation
from pywebio import *
from pywebio.output import *
from pywebio.input import *
from lloginPage import *

def altMode():
    
    #Railtrak logo
    put_image('https://i.imgur.com/y682Iqt.jpg', width='150px')
    put_button("Home", onclick=lambda: showMenu(), color='success', outline=True)

    #Trip information displayed
    put_markdown('# Trip 1(Houston - Dallas)')
    put_text('Current Map Path')
    
    #This is an image taken directly from Google Maps, might change later.
    put_image('https://www.google.com/maps/vt/data=aVjKhmJfFHs-olDWKtwvXJmDtQa08SVqGfO6rT5duov92S7Gp3pYGDyZLWmB9LTPcnp32r66yp5J8Pdo7ruoYbPXRKEooUkAJWXliW6bQ72Tl7B-9MUin5_itHwLafk3r3oiAA-8vHyElS7Wo40UqSUaOYSM94obwP-U7mdMjopbXw,I5UyRqn7K6QjC0-4l4g8lnUevTIjMjGzXpM0ux6ROnm4w_opo4e9gmxRs_BQD2f60ikRtB_P1yqg5mFstMiz5WeRUNW-Y0wMthmTreMmBskifDhsXdPVrjunA5I038qifE2YQO0T6CoO7LAOwZ1cEc0h_VYCYyTkIbU92yyYKVValoPWIqOq27ZVcanPB1vunS4rgoh8CHojPdOGo88ldy7jHlW7WBOQeAC5irq5Ti8pqW9DDhHMhRSPXgZlSkWHbIGSciXZe3bdqwEYNdfhsI-6Vq41BsB6qC4tKu4V4Khl0U-KL60sBJsYdBvWZXsaJ8VIe0a4INd7v7DyqVfswFxLGqnVWuCfvrrhzuOm?scale=1&h=200&w=652', width='1000px')
    put_warning('CURRENT ETA: 3 hours')

    #Dropbox of endpoint destination selections
    endpoint = select("Change route of transportation", ['Endpoint: Austin', 'Endpoint: College Station', 'Endpoint: Galveston'])

    #Checkbox to confirm it will replace old mode of transportation.
    checkbox("Confirm", options=['I UNDERSTAND IT WILL REPLACE OLD ROUTE OF TRANSPORTATION'])

    
    if 'Endpoint: Austin' in [endpoint]:
        put_markdown('# Updated Endpoint')
        put_image('https://www.google.com/maps/vt/data=a7GqHCXwHc5cxUlr86ux9ue7X_Z0icrRPN4dFW_g6cTEcW8OmemJCQSIHNc0U5AYOebR4x4gM6XNdpuKPW66Lg33i5op23iPosIeUYDZ9wn60OYARGIrlWkQWc8Y8-AKXfQ6YyTrmoxa8cKLy6iVircOatTp0B8xNMhzvL4K6tJSkA,rfVj1MmYX0y2w91LjqBu9QEuTq3Jjw-0JwFvSrrGv7RBkcr7eS_D0YCbonoud3BQelOe09XmPxudgtQhbLs5tvgSSmDsaLwwl2Pijg7op5515IADOkUXBiKPEZWkZY_aO6ecYGvvFRW-PLGppThJE1GzL1xq64I6n6tmkosLl3CuJdmp2Xld5k7tkGJgfGOepogbq5816FnGWFw8c_zgwD2803HeU7Mq73Bno96hKEmx1su6vZq_5yZDAWutEk_Sp8rPGXs9GcBZUUMVqZrASiQao3imAvcwcctKKWb-sjzQLcwIjnuOiegnLAITTos0O-Zc1HF67_-nNkLVeM3jCW6_XFa70Eyk1FXYfnO9?scale=1&h=200&w=652', width='1000px')

    if 'Endpoint: College Station' in [endpoint]:
        put_markdown('# Updated Endpoint')
        put_image('https://www.google.com/maps/vt/data=DFYvRMcM1bQLaZT_JyZ4Ol4mGXkGC82dOpz20wN4A7FARgEm96OywoZtAyo2DvgUxT-pHrlRRhr2owYMHYH9DkQqSl-gpaYd4OYrO66dC-AreQG4YcFjXmYmB-ueOl_mtB7WgWWkjrtWc1gNT9_MoAHGeUQHE_FoVJa96oCkkQqwzA,64gqUY2dZSwPrbp1zNDB2HcJfF-foNYdYg633jLa54JpAmMU7qw8CxD1wB0R6IzsmmyixRcXZgPTmcFrjg4AoL8NTZsZNrb2hXy6ykza_A5wnvHzpgU-av1v1JZRhHwTCMHagDssseXxjNSW9WJrIa9895_DnViNqga-_rqfnc3HQeSD0zmYP3Eku44ucBjBUYhpmBTQWooVWn_ErqpeXaO-hoxzfYs9hHSj3tRlIUXhn_OaM_o1D57fnKzZQ4pYGIWHiwgGpWLnJRgHb0uLSA2kxKtb83q1iERQKHJkKt8yJxc9DQWpts217fyizOAd4SG2lqDtM4f-zBzZN65FoVgxIdDE4fSWR7aUc-0KcIIjGZ7HebOkMQ?scale=1&h=200&w=652', width='1000px')
    
    if 'Endpoint: Galveston' in [endpoint]:
        put_markdown('# Updated Endpoint')
        put_image('https://www.google.com/maps/vt/data=4P8KN01rpePDExBh_tfIrz7WObXPh3vx3-lxltYyLmF3QhCUXjTcbzKvsQqo0wp2W-Dnu0JUW9KxRMAEZ6FOPHEcsA4ZrjupWDD6dznm3M972IOVoFUcBB7SywMP_tSJyUU_f9fAMcUQPOKPXdMUoIkHHY8Zz1nsN6I9dHqByS4wsw,BT4PY1EHhVc8Qhv6N6cuUqs9djr1u2dEnvGzvkdLC4I9kch_j6r_YVKI11vhNVSKWjLs3KlWN7R4TrcHu5GQxP9XgqKao4wp01rKVUDYsMWtGEIlaCQeI1FRNlncdmC_UIHVVuNp7p7HZ0NPFCzjNz6iFSiGsU9TgPim-XKORwuVkuX4cCXzg5owZ_WlF1yFcXUV94Ft762qXHC-RHCoHA90K6lHmxL-LSsfhK4qXuYJWyhb3E70DvY4vk09rOaMsrn9A7exXz8nMt13B64gyEzDwwT-IUqngNV8hPxRDYivPNXs3GfnK_EG7POcxC9hx3_LOmFsaFa9lPDweWStfgG9TkWvWJpK_5FLMaH03SU?scale=1&h=200&w=652', width='1000px')
