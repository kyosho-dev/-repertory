#include <allegro.h>
#include <stdlib.h>

//chamadas de funções pra esse bloco//
     void controles();
     void controlador_bola();

//variaveis goblais//

	 int x_barra1 = 5, y_barra1= 205; //1 jogador possição
	 int barra1_largura = 20, barra1_altura = 200;
	 
	 int x_barra2 = 775, y_barra2= 205; //2 jogador possição
	 int barra2_largura = 20, barra2_altura = 200;
	 
	 int x_bola = 390, y_bola= 300; // bola
	 int bola_largura = 10, bola_altura = 10;
	 int bola_velocidade_x, bola_velocidade_y;
	 int bola_direcao = 0; //direção 0 parado, 1 direita, 2 esquerda//
	 int bola_destroir = 0;
	 
	 int puntuacao1 = 0, puntuacao2 = 0;
	 int voltasM_1 = 0, voltasM_2 = 0;
	 int iniciou = 0;
	 
	 int venceu1 = 0, venceu2 = 0;


int main(){
	 //$inicializãção$//
	 
	 //instala os drives de comando//
	 allegro_init();
	 install_timer();
	 install_keyboard();
	 //seta a cor 32 bits/
	 set_color_depth(32);
	 //cria a janela//
	 set_gfx_mode(GFX_AUTODETECT_WINDOWED, 800, 600, 0, 0);
	 //comando que da titulo pro console//
	 set_window_title("Ping-pong");
	 
	 
	
	 BITMAP* buffer;// criador de quadros print//
	 buffer = create_bitmap(800, 600);
	 
	 //importa imagens
	 BITMAP* numero_0 = load_bitmap("n0.bmp", NULL);
	 BITMAP* numero_1 = load_bitmap("n1.bmp", NULL);
	 BITMAP* numero_2 = load_bitmap("n2.bmp", NULL);
	 BITMAP* numero_3 = load_bitmap("n3.bmp", NULL);
	 BITMAP* numero_4 = load_bitmap("n4.bmp", NULL);
	 BITMAP* numero_5 = load_bitmap("n5.bmp", NULL);
	 BITMAP* numero_6 = load_bitmap("n6.bmp", NULL);
	 BITMAP* numero_7 = load_bitmap("n7.bmp", NULL);
	 BITMAP* numero_8 = load_bitmap("n8.bmp", NULL);
	 BITMAP* numero_9 = load_bitmap("n9.bmp", NULL);
	 BITMAP* vecer1 = load_bitmap("titulo vencedor.bmp", NULL);
	 BITMAP* vecer2 = load_bitmap("titulo vencedor 2.bmp", NULL);
	 
	 
	 
	 
	 //comando que enserra o console se a condição sair do loop é durante o jogo//
	 while (!key[KEY_ESC]){
		
		
		//chamar as funções pro jogo//
		controles();
		controlador_bola();
		
		
		
		//cria as barras dos jogadores//
	    rectfill(buffer, x_barra1, y_barra1, x_barra1 + barra1_largura, y_barra1 + barra1_altura, makecol(255, 5, 50));
	    rectfill(buffer, x_barra2, y_barra2, x_barra2 + barra2_largura, y_barra2 + barra2_altura, makecol(30, 34, 202));
	    
	    //cria a divisoria/
		rectfill(buffer ,390, 1, 400, 600, makecol(75, 75, 75));
		
	    //cria a bola//
	    
	    if(bola_destroir == 0){
			rectfill(buffer, x_bola, y_bola, x_bola + bola_largura, y_bola + bola_altura, makecol(255, 255, 255));
			
	    }
	    
	    //coloca os sprites do contador jogador 1//
	    if(puntuacao1 == 0){
			draw_sprite (buffer, numero_0,100 ,10);
	    }
	    if(puntuacao1 == 1){
			draw_sprite (buffer, numero_1,100 ,10);
	    }
	    if(puntuacao1 == 2){
			draw_sprite (buffer, numero_2,100 ,10);
	    }
	    if(puntuacao1 == 3){
			draw_sprite (buffer, numero_3,100 ,10);
	    }
	    if(puntuacao1 == 4){
			draw_sprite (buffer, numero_4,100 ,10);
	    }
	    if(puntuacao1 == 5){
			draw_sprite (buffer, numero_5,100 ,10);
	    }
	    if(puntuacao1 == 6){
			draw_sprite (buffer, numero_6,100 ,10);
	    }
	    if(puntuacao1 == 7){
			draw_sprite (buffer, numero_7,100 ,10);
	    }
	    if(puntuacao1 == 8){
			draw_sprite (buffer, numero_8,100 ,10);
	    }
	    if(puntuacao1 == 9){
			draw_sprite (buffer, numero_9,100 ,10);
		}
		if(puntuacao1 == 10){
			
			draw_sprite (buffer, vecer1,210 ,10);
		}
		
	
	    //coloca os sprites do contador jogador 2//
	    
	    if(puntuacao2 == 0){
			draw_sprite (buffer, numero_0,700 ,10);
	    }
	    if(puntuacao2 == 1){
			draw_sprite (buffer, numero_1,700 ,10);
	    }
	    if(puntuacao2 == 2){
			draw_sprite (buffer, numero_2,700 ,10);
	    }
	    if(puntuacao2 == 3){
			draw_sprite (buffer, numero_3,700 ,10);
	    }
	    if(puntuacao2 == 4){
			draw_sprite (buffer, numero_4,700 ,10);
	    }
	    if(puntuacao2 == 5){
			draw_sprite (buffer, numero_5,700 ,10);
	    }
	    if(puntuacao2 == 6){
			draw_sprite (buffer, numero_6,700 ,10);
	    }
	    if(puntuacao2 == 7){
			draw_sprite (buffer, numero_7,700 ,10);
	    }
	    if(puntuacao2 == 8){
			draw_sprite (buffer, numero_8,700 ,10);
	    }
	    if(puntuacao2 == 9){
			draw_sprite (buffer, numero_9,700 ,10);
	    }
	    if(puntuacao2 == 10){
	    	
			draw_sprite (buffer, vecer2,400 ,10);
	    }
	    		 	
	    //função que passa o que esta armazenado na variavel buffer para a tela//
	    draw_sprite(screen, buffer, 0, 0);
		
		rest(0.5);
		clear (buffer);
			
	 }
	  
	 destroy_bitmap(buffer);
	 destroy_bitmap(numero_0);
	 destroy_bitmap(numero_1);
	 destroy_bitmap(numero_2);
	 destroy_bitmap(numero_3);
	 destroy_bitmap(numero_4);
	 destroy_bitmap(numero_5);
	 destroy_bitmap(numero_6);
	 destroy_bitmap(numero_7);
	 destroy_bitmap(numero_8);
	 destroy_bitmap(numero_9);
	 destroy_bitmap(vecer1);
	 destroy_bitmap(vecer2);
	 
	         
	 return 0;
}
END_OF_MAIN();


//seção de funçoes//

     void controles(){
			
			//comando  de impuit//
			
		    //jogador 1//
		    
		   if (key[KEY_UP] && y_barra1 > 0){ 
		   
			y_barra1 = y_barra1 - 2;
		   } 
		   if (key[KEY_DOWN] && y_barra1 + barra1_altura  < 600){
			 
			y_barra1 = y_barra1 + 2;
	       }
	       //jogador 2//
	       
		   if (key[KEY_W] && y_barra2 > 0){
		       
			y_barra2 = y_barra2 - 2;
		   } 
		   if (key[KEY_S] && y_barra2 + barra2_altura  < 600){
			   
			y_barra2 = y_barra2 + 2;
	       }
	       //start//
	       
	       if (key[KEY_ENTER] && iniciou == 0){
					
			iniciou = 1;
			bola_velocidade_x = 1 + rand() % 2;
			bola_velocidade_y = rand() % 2;
			bola_direcao = 1 + rand () % 2;
			rest(0.5);		
	       }
	       
	       //coloca o ponto pra 9//
	       
		   if (key[KEY_Q]){
					
			puntuacao1 = 9;		
	       }
			
     }
     void controlador_bola(){
			
	    //a bola foi destruida//
	    
	    if(bola_destroir == 1){
	    	
			bola_velocidade_x = 0;
			bola_velocidade_y = 0;
			x_bola = 390;
			y_bola= 300;
			rest(2);
			bola_destroir = 0;	
		}
	    //controlador da bola//
	    
	    if(bola_direcao == 1){	
	    
			x_bola = x_bola + bola_velocidade_x;
			y_bola = y_bola + bola_velocidade_y;
	    }
	      if(bola_direcao == 2){
		  	
			x_bola = x_bola - bola_velocidade_x;
			y_bola = y_bola + bola_velocidade_y;
	    }
	     ///colizor da bola //
	     
	    if (x_bola + bola_largura  > 800){
	    	
		   bola_direcao = 2; //X BARREIRA TELA//
		   puntuacao1 = puntuacao1 + 1;
		   bola_destroir = 1;
		   iniciou = 0;
		   
	    }
	    if (x_bola + bola_largura  < 0){
	    	
		   bola_direcao = 1;
		   puntuacao2 = puntuacao2 + 1;
		   bola_destroir = 1;
		   iniciou = 0;
	    }
	    if (y_bola + bola_altura  > 600){
	    	
		   bola_velocidade_y = -2; //Y BARREIRA TELA//
	    }
	    if (y_bola + bola_altura  < 0){
	    	
		   bola_velocidade_y = 2;
	    }
	    
	    //COLIZOR DA bolla com a barra//
	    
	    if (x_bola + bola_largura > x_barra2 && y_bola + bola_altura > y_barra2 && y_bola + bola_altura < y_barra2 + barra1_altura ){
	    	
			bola_direcao = 2;
			bola_velocidade_x = 1 + rand() % 2;
			bola_velocidade_y = 1 + rand() % 2;
	    }
	    
	    if (x_bola < x_barra1 + barra1_largura && y_bola + bola_altura > y_barra1 && y_bola + bola_altura < y_barra1 + barra1_altura ){
	    	
			bola_direcao = 1;
			bola_velocidade_x = 1 + rand() % 2;
			bola_velocidade_y = 1 + rand() % 2;
	    }
	    
     }

     
     
     
     
